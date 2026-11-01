# 02 — South-Facing Game Anchor (2.5D Real) — Zigo

**This is the most important image you will generate.** Every animation and every other direction is built from this. Get it right.

Unlike the pixel pipeline, the 2.5D Real anchor **uses box art as identity reference** — there is no pixel grid.

## When to use

- You have approved Zigo box art (step 01)
- You need a game-ready south-facing sprite with painted volume and consistent lighting

## Inputs

- **Text prompt** (below)
- **Image 1** — approved box art `zigo/select.jpg`

> Do pass the box art here. Translate the portrait into a centered full-body game sprite. Do not copy the rooftop composition.

## Prompt (copy & paste)

```text
Intended use: a single south-facing idle sprite frame for a top-down 2.5D action game on a flat 2D map. Final artwork should behave like one logical 256x256 in-game frame, delivered at 1024x1024 with readable painted volume at game scale.

Image 1 role: identity anchor. Preserve this exact character identity, palette, costume, prop design, silhouette logic, and top-left lighting direction. Translate the portrait into a centered full-body game sprite — do not copy the portrait composition literally.

Subject:
- Zigo, Feline Rogue, facing SOUTH directly toward the camera in 3/4 top-down game perspective.
- This is the canonical idle frame.
- Compact bipedal cat silhouette in the low crouch from Image 1: short-haired cream and light-grey tabby, dark stripes on forehead and cheeks, bright cyan-blue eyes, pink nose, white muzzle and chest, ringed cream tail. The head, leather vest, bow on the back, and tail must all read when scaled down.
- Brown leather rogue kit from Image 1: fitted vest with a diagonal chest strap and buckle, metal pauldrons on both shoulders, leather bracers, a belt with a buckle and a side pouch, and a short chainmail hem. Pale shirt sleeves under the leather. Dark trousers. Bare feline paws on hands and feet. No boots, cloak, or hood.
- A wooden recurve bow is slung on his back, as in Image 1, with the upper limb above one shoulder. A quiver of fletched arrows sits on his back over the other shoulder. Both paws stay empty. The bow is not in his hands and no arrow is on the string.
- Keep the low crouch from Image 1: one paw planted forward, the other near the waist. Watchful gaze. Paws stay readable.

Frame rules:
- One character only, centered.
- Full body visible, square 1024x1024 canvas.
- Visible body fits within the intended logical sprite box.
- Anchor/foot plant at bottom-center.
- Preserve idle readability, not an attack pose.
- Both feet visible and grounded, with no floor under them.

Style:
- pre-rendered 2.5D game sprite — painted fantasy illustration, not pixel art
- readable volume: soft shading on tabby fur, leather, and the bow
- one light only, from the top-left
- clean edges with controlled anti-aliasing — no muddy painterly blur
- character reads clearly when scaled down to 256x256

Background:
- solid flat chroma color #00FF00 (green)
- absolutely no ground shadow, floor plane, gradient, or environment
- no scenery, props, borders, UI, text, logo, or watermark

Avoid:
- the Gothic rooftop, rain, cables, neon signs, and the letters from Image 1
- pixel art, SNES-style blocks, or chunky pixel clusters
- photorealistic fur strands or hyper-textured materials
- the bow in his paws, a drawn bow, a loosed arrow, magic glow, aura, or particles
- dramatic camera angles or perspective distortion
- extra characters
```

## Recommended sizes

- Logical frame size = `256×256`
- Output size = `1024×1024` square

## Notes

- Attach `zigo/select.jpg` as Image 1. The text alone will drift the costume.
- The green plate is `#00FF00`, flat, with no floor and no contact shadow. A shadow under the feet means the frame is rejected.
- Generate 2–4 variants and pick the one with the cleanest silhouette, the most stable foot baseline, and the closest match to the box art.
- Keep the bow on his back, as in `zigo/select.jpg`. Both paws stay empty. The full draw belongs in the attack sheet.

## Next step

→ [03 — Neutral Anchor Reset](03-neutral-anchor.md)
