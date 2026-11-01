"""Cut a flat #00FF00 plate to straight RGBA without a green halo.

Background is only green that touches the image border. Interior cyan
(rune trim) is left alone. Edge pixels are unmixed so the stored color
is the character, not character-plus-green.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

KEY = np.array([0.0, 1.0, 0.0], dtype=np.float64)
HARD_EXCESS = 0.45
SOFT_LO = 0.04
SOFT_HI = 0.45
FRINGE = 3
BLEED = 2


def green_excess(rgb: np.ndarray) -> np.ndarray:
    return rgb[..., 1] - np.maximum(rgb[..., 0], rgb[..., 2])


def border_background(hard: np.ndarray) -> np.ndarray:
    labels, _ = ndimage.label(hard)
    if labels.max() == 0:
        return np.zeros(hard.shape, dtype=bool)
    edges = np.concatenate(
        [labels[0, :], labels[-1, :], labels[:, 0], labels[:, -1]]
    )
    keep = np.unique(edges)
    keep = keep[keep != 0]
    return np.isin(labels, keep)


def dilate(mask: np.ndarray, radius: int) -> np.ndarray:
    if radius <= 0:
        return mask
    return ndimage.binary_dilation(mask, iterations=radius)


def smoothstep(edge0: float, edge1: float, value: np.ndarray) -> np.ndarray:
    t = np.clip((value - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def plate_key(rgb: np.ndarray) -> np.ndarray:
    """Measured border green. A plate near #00FF00 still shifts the fringe if unmixed against pure green."""
    border = np.concatenate([rgb[0], rgb[-1], rgb[:, 0], rgb[:, -1]], axis=0)
    key = np.median(border, axis=0)
    if float(green_excess(key)) < 0.5:
        return KEY.copy()
    return key


def unmix(rgb: np.ndarray, alpha: np.ndarray, key: np.ndarray | None = None) -> np.ndarray:
    scale = np.maximum(alpha, 1e-4)[..., None]
    foreground = (rgb - (1.0 - alpha)[..., None] * (KEY if key is None else key)) / scale
    return np.clip(foreground, 0.0, 1.0)


def bleed_color(rgb: np.ndarray, alpha: np.ndarray, radius: int) -> np.ndarray:
    color = rgb.copy()
    filled = alpha > 0.01
    for _ in range(radius):
        padded = np.pad(color, ((1, 1), (1, 1), (0, 0)), mode="edge")
        mask = np.pad(filled, 1, mode="constant", constant_values=False)
        acc = np.zeros_like(color)
        weight = np.zeros(color.shape[:2], dtype=np.float64)
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neighbor = padded[1 + dy : 1 + dy + color.shape[0], 1 + dx : 1 + dx + color.shape[1]]
            neighbor_on = mask[1 + dy : 1 + dy + color.shape[0], 1 + dx : 1 + dx + color.shape[1]]
            acc += neighbor * neighbor_on[..., None]
            weight += neighbor_on
        take = (~filled) & (weight > 0)
        color[take] = acc[take] / weight[take, None]
        filled = filled | take
    return color


def despill_rgba(rgb: np.ndarray, alpha: np.ndarray) -> tuple[np.ndarray, np.ndarray, dict]:
    """Remove green left on an already-transparent cut. Cyan stays: its blue channel is at least as high as green."""
    rgb = np.clip(rgb.astype(np.float64), 0.0, 1.0)
    alpha = np.clip(alpha.astype(np.float64), 0.0, 1.0)
    excess = np.clip(green_excess(rgb), 0.0, None)
    peak = np.maximum(rgb[..., 0], rgb[..., 2])
    mix = np.clip(excess / np.maximum(1.0 - peak, 1e-3), 0.0, 1.0)

    foreground = rgb.copy()
    foreground[..., 1] = np.minimum(rgb[..., 1], peak)

    cleaned = alpha.copy()
    leftover = (mix > 0.65) & (alpha < 0.9)
    cleaned[leftover] = alpha[leftover] * (1.0 - mix[leftover])

    visible = cleaned > 0.05
    report = {
        "mode": "despill",
        "background_pixels": int((cleaned <= 0.01).sum()),
        "semi_pixels": int(((cleaned > 0.02) & (cleaned < 0.98)).sum()),
        "max_excess_on_opaque": float(green_excess(foreground)[visible].max() if np.any(visible) else 0.0),
        "mean_excess_on_soft_color": 0.0,
    }
    report["ok"] = report["max_excess_on_opaque"] <= 0.02
    return np.clip(foreground, 0.0, 1.0), np.clip(cleaned, 0.0, 1.0), report


def cut_rgba(rgba: np.ndarray) -> tuple[np.ndarray, np.ndarray, dict]:
    rgb = rgba[..., :3]
    alpha = rgba[..., 3] if rgba.shape[-1] == 4 else np.ones(rgb.shape[:2], dtype=np.float64)
    border_alpha = np.concatenate([alpha[0, :], alpha[-1, :], alpha[:, 0], alpha[:, -1]])
    border_excess = green_excess(rgb)
    border_excess = np.concatenate(
        [border_excess[0, :], border_excess[-1, :], border_excess[:, 0], border_excess[:, -1]]
    )
    already_cut = float(np.percentile(border_alpha, 90)) < 0.05 and float(np.percentile(border_excess, 90)) < 0.15
    if already_cut:
        return despill_rgba(rgb, alpha)
    foreground, alpha_out, report = cut_rgb(rgb)
    report["mode"] = "plate"
    return foreground, alpha_out, report


def cut_rgb(rgb: np.ndarray) -> tuple[np.ndarray, np.ndarray, dict]:
    rgb = np.clip(rgb.astype(np.float64), 0.0, 1.0)
    key = plate_key(rgb)
    excess = green_excess(rgb)
    background = border_background(excess > HARD_EXCESS)
    # A closed guard can trap a patch of the plate. That green never touches the border.
    dist = np.max(np.abs(rgb - key), axis=-1)
    background = background | ((excess > HARD_EXCESS) & (dist < 0.2))
    band = dilate(background, FRINGE) & ~background

    alpha = np.ones(excess.shape, dtype=np.float64)
    alpha[background] = 0.0
    alpha[band] = 1.0 - smoothstep(SOFT_LO, SOFT_HI, excess[band])

    foreground = rgb.copy()
    soft = alpha < 0.999
    foreground[soft] = unmix(rgb, alpha, key)[soft]
    foreground = bleed_color(foreground, alpha, BLEED)

    semi = (alpha > 0.02) & (alpha < 0.98)
    report = {
        "background_pixels": int(background.sum()),
        "semi_pixels": int(semi.sum()),
        "max_excess_on_opaque": float(excess[alpha > 0.95].max() if np.any(alpha > 0.95) else 0.0),
        "mean_excess_on_soft_color": float(
            green_excess(foreground)[semi].mean() if np.any(semi) else 0.0
        ),
    }
    report["ok"] = (
        report["max_excess_on_opaque"] < 0.2
        and report["mean_excess_on_soft_color"] < 0.08
        and report["background_pixels"] > 0
    )
    return np.clip(foreground, 0.0, 1.0), np.clip(alpha, 0.0, 1.0), report


def load_rgba(path: Path) -> np.ndarray:
    image = Image.open(path).convert("RGBA")
    return np.asarray(image).astype(np.float64) / 255.0


def save_rgba(path: Path, rgb: np.ndarray, alpha: np.ndarray) -> None:
    rgba = np.dstack([rgb, alpha])
    out = (np.clip(rgba, 0.0, 1.0) * 255.0).round().astype(np.uint8)
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(out, mode="RGBA").save(path)


def composite(rgb: np.ndarray, alpha: np.ndarray, color: tuple[float, float, float]) -> np.ndarray:
    plate = np.array(color, dtype=np.float64)
    return rgb * alpha[..., None] + plate * (1.0 - alpha[..., None])


def iter_inputs(path: Path) -> list[Path]:
    if path.is_dir():
        files = sorted(path.glob("*.png"))
        if not files:
            raise SystemExit(f"No PNG files in {path}")
        return files
    return [path]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Cut flat #00FF00 frames without a green halo.")
    parser.add_argument("input", type=Path, help="PNG file or a directory of PNGs")
    parser.add_argument("-o", "--output", type=Path, required=True, help="PNG file or output directory")
    parser.add_argument("--qa", action="store_true", help="Write black and white composites beside each cut")
    args = parser.parse_args(argv)

    sources = iter_inputs(args.input)
    many = args.input.is_dir() or len(sources) > 1
    if many and args.output.suffix.lower() == ".png":
        raise SystemExit("Output must be a directory when cutting more than one frame.")

    failed = 0
    for source in sources:
        rgb, alpha, report = cut_rgba(load_rgba(source))
        dest = args.output / source.name if many else args.output
        save_rgba(dest, rgb, alpha)
        status = "ok" if report["ok"] else "FAIL"
        print(
            f"{status} {report.get('mode', 'plate')} {source.name} "
            f"semi={report['semi_pixels']} "
            f"opaque_excess={report['max_excess_on_opaque']:.3f} "
            f"soft_excess={report['mean_excess_on_soft_color']:.3f}"
        )
        if args.qa:
            qa_dir = dest.parent / "qa"
            save_rgba(qa_dir / f"{dest.stem}-white.png", composite(rgb, alpha, (1, 1, 1)), np.ones_like(alpha))
            save_rgba(qa_dir / f"{dest.stem}-black.png", composite(rgb, alpha, (0, 0, 0)), np.ones_like(alpha))
        if not report["ok"]:
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
