# 02 — South-Facing Game Anchor (2.5D Real)

**This is the most important image you will generate.** Every animation and every other direction is built from this. Get it right.

Unlike the [pixel pipeline](../old/pixel-tutorial/prompts/02-south-anchor.md), the 2.5D Real anchor **uses box art as identity reference** — there is no pixel grid.

## When to use

- You have approved box art (step 01)
- You need a game-ready south-facing sprite with painted volume and consistent lighting

## Inputs

- **Text prompt** (template below)
- **Image 1** — approved box art from step 01 (identity, palette, silhouette, lighting)

> ⚠️ **Do pass box art here.** In 2.5D Real, the goal is painted volume — box art is the right identity anchor. The pixel pipeline rejects this path; this one embraces it.

## Prompt template

```text
Intended use: a single south-facing idle sprite frame for a top-down 2.5D action game on a flat 2D map. Final artwork should behave like one logical {LOGICAL_FRAME_SIZE} in-game frame, delivered at {OUTPUT_SIZE} with readable painted volume at game scale.

Image 1 role: identity anchor. Preserve this exact character identity, palette, costume, prop design, silhouette logic, and lighting direction. Translate the portrait into a centered full-body game sprite — do not copy the portrait composition literally.

Subject:
- {CHARACTER_NAME}, {ARCHETYPE}, facing SOUTH directly toward the camera in 3/4 top-down game perspective.
- This is the canonical idle frame.
- {SILHOUETTE_NOTES}
- {COSTUME_DETAILS}
- {PROP_DETAILS}
- calm readable idle expression/pose.

Frame rules:
- One character only, centered.
- Full body visible.
- Visible body fits within the intended logical sprite box.
- Anchor/foot plant at bottom-center.
- Preserve idle readability, not an attack pose.
- Both feet visible and grounded.

Style:
- pre-rendered 2.5D game sprite — painted fantasy illustration, not pixel art
- readable volume: soft shading, costume folds, material separation
- consistent top-left light source (match Image 1)
- clean edges with controlled anti-aliasing — no muddy painterly blur
- character reads clearly when scaled down to {LOGICAL_FRAME_SIZE}

Background:
- solid flat chroma color, preferably #00FF00 (green) — keys better on soft edges than magenta
- absolutely no ground shadow, floor plane, gradient, or environment
- no scenery, props, borders, UI, text, logo, or watermark

Avoid:
- pixel art, SNES-style blocks, or chunky pixel clusters
- photorealistic skin or hyper-textured materials
- baked-in magic orb, aura, particles, or casting effects
- dramatic camera angles or perspective distortion
- extra characters
```

## Recommended sizes

- `{LOGICAL_FRAME_SIZE}` = `256x256` (default) or `512x512` (more detail, larger atlases)
- `{OUTPUT_SIZE}` = `1024x1024` (for 256 logical) or `1024x1024`–`1536x1536` (for 512 logical)

## Notes

- Prefer **green chroma `#00FF00`** over magenta — soft painted edges key out more cleanly from green in most BG-removal tools.
- Generate **2–4 variants** and pick the one with the cleanest silhouette, most stable foot baseline, and best match to box art.
- Output will have soft anti-aliased edges — that's expected. Normalization (step 08) handles cleanup.

## Next step

→ [03 — Neutral Anchor Reset](03-neutral-anchor.md)
