"""Synthetic plate: green screen, navy body, interior cyan rune, green-mixed edge."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cut_chroma import cut_rgba, cut_rgb, green_excess


def plate() -> np.ndarray:
    rgb = np.zeros((48, 48, 3), dtype=np.float64)
    rgb[..., 1] = 1.0
    body = np.array([0.08, 0.12, 0.45])
    rgb[12:36, 14:34] = body
    rgb[20:24, 22:28] = (0.05, 0.85, 0.95)
    rgb[12:36, 14] = body * 0.60 + np.array([0.0, 1.0, 0.0]) * 0.40
    return rgb


def main() -> int:
    src = plate()
    rgb, alpha, report = cut_rgb(src)

    assert alpha[0, 0] == 0.0, "corner green must be transparent"
    assert alpha[22, 24] > 0.95, "interior cyan rune must stay opaque"
    rune = rgb[22, 24]
    assert rune[2] > rune[0] + 0.4, "rune must stay cyan"
    assert 0.05 < alpha[20, 14] < 0.95, "mixed edge must be partial alpha"
    assert green_excess(rgb)[20, 14] < 0.08, "mixed edge must be despilled"
    assert report["ok"], report
    print("plate", report)

    rgba = np.zeros((24, 24, 4), dtype=np.float64)
    rgba[8:16, 8:16, :3] = (0.55, 0.55, 0.58)
    rgba[8:16, 8:16, 3] = 1.0
    rgba[10:13, 10:14, :3] = (0.05, 0.85, 0.95)
    rgba[10:13, 10:14, 3] = 1.0
    rgba[8:16, 8, :3] = (0.45, 0.80, 0.42)
    rgba[8:16, 8, 3] = 0.85
    rgb, alpha, report = cut_rgba(rgba)
    assert report["mode"] == "despill"
    assert alpha[0, 0] == 0.0
    assert alpha[11, 12] > 0.95
    assert rgb[11, 12, 2] > 0.9
    assert green_excess(rgb)[12, 8] <= 0.02
    assert report["ok"], report
    print("despill", report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
