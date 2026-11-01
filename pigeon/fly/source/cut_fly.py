"""Cut the fly sheet. JPEG green is not #00FF00, so unmix against the measured plate."""

from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / ".cursor/skills/cut-chroma-frames/scripts"))
import cut_chroma as cc

ROOT = Path(__file__).resolve().parent.parent
src_path = ROOT / "source" / "sheet.jpg"
frames_dir = ROOT / "frames"
qa_dir = ROOT / "qa"
frames_dir.mkdir(exist_ok=True)
qa_dir.mkdir(exist_ok=True)

src = np.asarray(Image.open(src_path).convert("RGB")).astype(np.float64) / 255.0
border = np.concatenate([src[0], src[-1], src[:, 0], src[:, -1]], axis=0)
key = np.median(border, axis=0)
key_excess = float(cc.green_excess(key.reshape(1, 1, 3))[0, 0])
excess = cc.green_excess(src)
background = cc.border_background(excess > 0.55)
labels, n = ndimage.label((excess > 0.70) & ~background)
for i in range(1, n + 1):
    pocket = labels == i
    if pocket.sum() < 400:
        background |= pocket

band = cc.dilate(background, 2) & ~background
alpha = np.ones(excess.shape, dtype=np.float64)
alpha[background] = 0.0
alpha[band] = 1.0 - np.clip(excess[band] / max(key_excess, 1e-3), 0.0, 1.0)
foreground = src.copy()
scale = np.maximum(alpha[band], 1e-3)[..., None]
foreground[band] = np.clip((src[band] - (1.0 - alpha[band])[..., None] * key) / scale, 0.0, 1.0)

# Split where the column of bird pixels is thinnest, expecting six bodies.
solid = alpha > 0.35
cols = solid.mean(axis=0)
windows = [(140, 175), (270, 330), (480, 545), (650, 710), (820, 860)]
cuts = [0]
for lo, hi in windows:
    cuts.append(lo + int(np.argmin(cols[lo:hi])))
cuts.append(src.shape[1])
print("cuts", cuts)

pad = 6
pieces = []
for i in range(len(cuts) - 1):
    x0, x1 = cuts[i], cuts[i + 1] - 1
    slab_a = alpha[:, x0 : x1 + 1]
    slab_rgb = foreground[:, x0 : x1 + 1]
    labels, n = ndimage.label(slab_a > 0.35)
    if n == 0:
        continue
    counts = np.bincount(labels.ravel())
    counts[0] = 0
    keep = labels == int(np.argmax(counts))
    ys, xs = np.where(keep)
    y0, y1 = int(ys.min()), int(ys.max())
    bx0, bx1 = int(xs.min()), int(xs.max())
    crop_a = np.zeros_like(slab_a)
    crop_rgb = np.zeros_like(slab_rgb)
    crop_a[keep] = slab_a[keep]
    crop_rgb[keep] = slab_rgb[keep]
    # include the soft fringe of this body only
    fringe = ndimage.binary_dilation(keep, iterations=2) & (slab_a > 0.02)
    crop_a[fringe] = slab_a[fringe]
    crop_rgb[fringe] = slab_rgb[fringe]
    crop_rgb = crop_rgb[max(0, y0 - 2) : y1 + 3, max(0, bx0 - 2) : bx1 + 3]
    crop_a = crop_a[max(0, y0 - 2) : y1 + 3, max(0, bx0 - 2) : bx1 + 3]
    pieces.append((crop_rgb, crop_a, y1 - y0))

cell_w = max(p[0].shape[1] for p in pieces) + pad * 2
cell_h = max(p[0].shape[0] for p in pieces) + pad * 2
foot = cell_h - pad - 1
print("cell", cell_w, cell_h, "frames", len(pieces))

canvases = []
for i, (crop_rgb, crop_a, _) in enumerate(pieces):
    canvas_rgb = np.zeros((cell_h, cell_w, 3), dtype=np.float64)
    canvas_a = np.zeros((cell_h, cell_w), dtype=np.float64)
    sh, sw = crop_a.shape
    opaque_rows = np.where((crop_a > 0.5).any(axis=1))[0]
    local_bottom = int(opaque_rows.max())
    dest_top = foot - local_bottom
    dest_x = (cell_w - sw) // 2
    canvas_rgb[dest_top : dest_top + sh, dest_x : dest_x + sw] = crop_rgb
    canvas_a[dest_top : dest_top + sh, dest_x : dest_x + sw] = crop_a

    solid = canvas_a > 0.5
    dist = ndimage.distance_transform_edt(solid)
    excess = canvas_rgb[..., 1] - np.maximum(canvas_rgb[..., 0], canvas_rgb[..., 2])
    rim = solid & (dist <= 6) & (excess > 0.02)
    peak = np.maximum(canvas_rgb[..., 0], canvas_rgb[..., 2])
    canvas_rgb[..., 1] = np.where(rim, np.minimum(canvas_rgb[..., 1], peak), canvas_rgb[..., 1])

    dist, (iy, ix) = ndimage.distance_transform_edt(~solid, return_indices=True)
    near = (dist > 0) & (dist <= 2)
    canvas_rgb[near] = canvas_rgb[iy[near], ix[near]]
    far = dist > 2
    fill = np.median(canvas_rgb[near], axis=0) if near.any() else np.array([0.45, 0.45, 0.4])
    canvas_rgb[far] = fill
    canvas_a[far] = 0.0

    out = np.dstack([np.clip(canvas_rgb, 0, 1), np.clip(canvas_a, 0, 1)])
    Image.fromarray((out * 255).round().astype(np.uint8), "RGBA").save(frames_dir / f"fly_{i:02d}.png")
    yy = np.where(canvas_a > 0.5)[0]
    print(i, "bottom", int(yy.max()), "top", int(yy.min()), "px", int((canvas_a > 0.5).sum()))
    canvases.append(out)

sheet = np.concatenate(canvases, axis=1)
rgb, al = sheet[..., :3], sheet[..., 3]
mag = np.zeros_like(rgb)
mag[..., 0] = 1
mag[..., 2] = 1
Image.fromarray((np.clip(rgb * al[..., None] + mag * (1 - al[..., None]), 0, 1) * 255).round().astype(np.uint8), "RGB").save(qa_dir / "frames-magenta.png")
Image.fromarray((np.clip(rgb * al[..., None], 0, 1) * 255).round().astype(np.uint8), "RGB").save(qa_dir / "frames-black.png")
Image.fromarray((np.clip(rgb * al[..., None] + (1 - al[..., None]), 0, 1) * 255).round().astype(np.uint8), "RGB").save(qa_dir / "frames-white.png")
