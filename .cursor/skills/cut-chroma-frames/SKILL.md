---
name: cut-chroma-frames
description: Cuts flat #00FF00 character frames to RGBA without a green halo, and keeps interior cyan costume details such as rune trim. Use when extracting sprite frames, removing a green screen, or when a cutout shows a green fringe, edge spill, or eaten cyan trim.
---

# Cut chroma frames

Run the script. Do not key by deleting every green pixel. Interior cyan is costume.

```bash
python .cursor/skills/cut-chroma-frames/scripts/cut_chroma.py FRAMES -o cut --qa
```

`FRAMES` is one PNG or a directory of PNGs. The plate must be flat `#00FF00` with no floor and no contact shadow. A shadow under the feet means the video is rejected, not that this script should try harder.

On a flat green plate, the script keys only the green that touches the image border and unmixes the fringe. On a PNG that is already transparent, it despills green left in the edge color. A cyan rune stays, because its blue channel is at least as high as its green. The fringe color is bled into transparent pixels so scaling does not resample green or black.

Check the printed line. `FAIL` means opaque pixels are still green or the soft edge is still contaminated. Look at `qa/*-white.png` (green halo) and `qa/*-black.png` (holes in the rune or the fur). Do not pass a failed frame into Sprite Smithy.

Needs numpy, Pillow, and scipy.
