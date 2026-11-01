"""Cut the clean six-bird fly sheet. Plate green is JPEG-like, not #00FF00."""

from pathlib import Path
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / ".cursor/skills/cut-chroma-frames/scripts"))
import cut_chroma as cc

ROOT = Path(__file__).resolve().parent.parent
src = np.asarray(Image.open(ROOT / "source" / "sheet-good.png").convert("RGB")).astype(np.float64) / 255.0
border = np.concatenate([src[0], src[-1], src[:, 0], src[:, -1]], axis=0)
key = np.median(border, axis=0)
key_excess = float(cc.green_excess(key.reshape(1, 1, 3))[0, 0])
excess = cc.green_excess(src)
background = cc.border_background(excess > 0.50)
band = cc.dilate(background, 2) & ~background
alpha = np.ones(excess.shape, dtype=np.float64)
alpha[background] = 0.0
alpha[band] = 1.0 - np.clip(excess[band] / max(key_excess, 1e-3), 0.0, 1.0)
rgb = src.copy()
scale = np.maximum(alpha[band], 1e-3)[..., None]
rgb[band] = np.clip((src[band] - (1.0 - alpha[band])[..., None] * key) / scale, 0.0, 1.0)

char = ndimage.binary_opening(alpha > 0.45, iterations=1)
labels, n = ndimage.label(char)
boxes = []
for i in range(1, n + 1):
    ys, xs = np.where(labels == i)
    if len(xs) < 2000:
        continue
    boxes.append((int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()), i))
boxes.sort()
assert len(boxes) == 6, len(boxes)

h, w = alpha.shape
pad = 8
crops = []
for index, (x0, y0, x1, y1, label) in enumerate(boxes):
    left = 0 if index == 0 else (boxes[index - 1][2] + x0) // 2
    right = w - 1 if index == 5 else (x1 + boxes[index + 1][0]) // 2
    top = max(0, y0 - 3)
    bottom = min(h - 1, y1 + 3)
    cx0 = max(left, x0 - 2)
    cx1 = min(right, x1 + 2)
    mask = ndimage.binary_dilation(labels == label, iterations=2)
    crop_a = np.where(mask[top : bottom + 1, cx0 : cx1 + 1], alpha[top : bottom + 1, cx0 : cx1 + 1], 0.0)
    crop_rgb = np.where(mask[top : bottom + 1, cx0 : cx1 + 1, None], rgb[top : bottom + 1, cx0 : cx1 + 1], 0.0)
    crops.append((crop_rgb, crop_a, top))

cell_w = max(c[0].shape[1] for c in crops) + pad * 2
cell_h = h
frames_dir = ROOT / "frames"
qa_dir = ROOT / "qa"
frames_dir.mkdir(exist_ok=True)
qa_dir.mkdir(exist_ok=True)
for old in frames_dir.glob("fly_*.png"):
    old.unlink()

canvases = []
for i, (crop_rgb, crop_a, top) in enumerate(crops):
    canvas_rgb = np.zeros((cell_h, cell_w, 3), dtype=np.float64)
    canvas_a = np.zeros((cell_h, cell_w), dtype=np.float64)
    sh, sw = crop_a.shape
    dest_x = (cell_w - sw) // 2
    canvas_rgb[top : top + sh, dest_x : dest_x + sw] = crop_rgb
    canvas_a[top : top + sh, dest_x : dest_x + sw] = crop_a

    solid = canvas_a > 0.5
    dist = ndimage.distance_transform_edt(solid)
    ex = canvas_rgb[..., 1] - np.maximum(canvas_rgb[..., 0], canvas_rgb[..., 2])
    rim = solid & (dist <= 5) & (ex > 0.02)
    peak = np.maximum(canvas_rgb[..., 0], canvas_rgb[..., 2])
    canvas_rgb[..., 1] = np.where(rim, np.minimum(canvas_rgb[..., 1], peak), canvas_rgb[..., 1])

    outside = ~solid
    _, (iy, ix) = ndimage.distance_transform_edt(outside, return_indices=True)
    near = outside & (ndimage.distance_transform_edt(outside) <= 2)
    canvas_rgb[near] = canvas_rgb[iy[near], ix[near]]
    far = ndimage.distance_transform_edt(outside) > 2
    fill = np.median(canvas_rgb[near], axis=0) if near.any() else np.array([0.45, 0.45, 0.42])
    canvas_rgb[far] = fill
    canvas_a[far] = 0.0

    parts = ndimage.label(canvas_a > 0.2)[0]
    counts = np.bincount(parts.ravel())
    counts[0] = 0
    if counts.size > 1:
        keep = parts == int(np.argmax(counts))
        canvas_a[(parts != 0) & ~keep] = 0.0

    out = np.dstack([np.clip(canvas_rgb, 0, 1), np.clip(canvas_a, 0, 1)])
    Image.fromarray((out * 255).round().astype(np.uint8), "RGBA").save(frames_dir / f"fly_{i:02d}.png")
    ys = np.where(canvas_a > 0.5)[0]
    xs = np.where(canvas_a > 0.5)[1]
    ex2 = canvas_rgb[..., 1] - np.maximum(canvas_rgb[..., 0], canvas_rgb[..., 2])
    tr = canvas_a < 0.02
    print(
        i,
        "y",
        int(ys.min()),
        int(ys.max()),
        "x",
        int(xs.min()),
        int(xs.max()),
        "trans_ex",
        round(float(ex2[tr].mean()), 3),
        "parts",
        int(ndimage.label(canvas_a > 0.2)[1]),
    )
    canvases.append(out)

sheet = np.concatenate(canvases, axis=1)
rgb, al = sheet[..., :3], sheet[..., 3]
mag = np.zeros_like(rgb)
mag[..., 0] = 1.0
mag[..., 2] = 1.0
Image.fromarray((np.clip(rgb * al[..., None] + mag * (1 - al[..., None]), 0, 1) * 255).round().astype(np.uint8), "RGB").save(qa_dir / "good-magenta.png")
Image.fromarray((np.clip(rgb * al[..., None], 0, 1) * 255).round().astype(np.uint8), "RGB").save(qa_dir / "good-black.png")
Image.fromarray((np.clip(rgb * al[..., None] + (1 - al[..., None]), 0, 1) * 255).round().astype(np.uint8), "RGB").save(qa_dir / "good-white.png")
