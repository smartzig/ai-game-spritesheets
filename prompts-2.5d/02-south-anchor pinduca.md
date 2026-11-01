# 02 — South-Facing Game Anchor (2.5D Real) — Pinduca

**This is the most important image you will generate.** Every animation and every other direction is built from this. Get it right.

Unlike the [pixel pipeline](../old/pixel-tutorial/prompts/02-south-anchor%20pinduca.md), the 2.5D Real anchor **uses box art as identity reference** — there is no pixel grid.

## When to use

- You have approved Pinduca box art (step 01)
- You need a game-ready south-facing sprite with painted volume and consistent lighting

## Inputs

- **Text prompt** (template below)
- **Image 1** — approved box art from [01 — Box Art](01-box-art%20pinduca.md) (`pinduca/pinduca-box1.png` or your best variant)

> ✅ **Do pass box art here.** In 2.5D Real, box art is the right identity anchor. Translate portrait → centered full-body game sprite.



## Prompt (copy & paste)

```text
Intended use: a single south-facing idle sprite frame for a top-down 2.5D action game on a flat 2D map. Final artwork should behave like one logical 256x256 in-game frame, delivered at 1024x1024 with readable painted volume at game scale.

Image 1 role: identity anchor. Preserve this exact character identity, palette, costume, prop design, silhouette logic, and top-left lighting direction. Translate the portrait into a centered full-body game sprite — do not copy the portrait composition literally.

Subject:
- Pinduca, Mystical Feline Mage, facing SOUTH directly toward the camera in 3/4 top-down game perspective.
- This is the canonical idle frame.
- Compact upright bipedal cat silhouette: oversized fluffy head and white ruff, long navy robe hem, bushy ringed grey-white tail — all must read when scaled down.
- Deep navy/royal blue hooded wizard robe (hood down on shoulders), cyan glowing rune trim on cuffs/front opening/hem, blue waist sash, lighter blue V-neck underlayer; grey-and-white tabby fur face with sapphire-blue eyes; unarmored paws visible.
- No staff or physical weapon. Paws free and readable for somatic casting — do not bake a large magic orb, glow, or particles into this idle frame.
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
- readable volume: soft shading on tabby fur, white ruff, robe folds, and sash
- consistent top-left light source (match Image 1)
- clean edges with controlled anti-aliasing — no muddy painterly blur
- character reads clearly when scaled down to 256x256

Background:
- solid flat chroma color #00FF00 (green) 
- absolutely no ground shadow, floor plane, gradient, or environment
- no scenery, props, borders, UI, text, logo, or watermark

Avoid:
- pixel art, SNES-style blocks, or chunky pixel clusters
- photorealistic fur strands or hyper-textured materials
- baked-in magic orb, aura, particles, or casting effects
- dramatic camera angles or perspective distortion
- extra characters
```



## Recommended sizes

- Logical frame size = `256×256`
- Output size = `1024×1024`



## Notes

- Prefer **green chroma** `#00FF00` — soft painted edges on ruff and tail key out more cleanly from green.
- Generate **2–4 variants** and pick the one with the cleanest silhouette, most stable foot baseline, and best match to box art.
- Keep cyan robe runes as **costume trim** with gentle glow — identity, not a dynamic attack effect.
- Output will have soft anti-aliased edges — expected. Normalization (step 08) handles cleanup.



## Next step

→ [03 — Neutral Anchor Reset](03-neutral-anchor%20pinduca.md)