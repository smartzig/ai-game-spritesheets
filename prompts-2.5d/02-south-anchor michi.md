# 02 — South-Facing Game Anchor (2.5D Real) — Michi

Esboço. Ainda não foi gerado. O select aprovado trava a identidade. Este texto só traduz essa imagem para o sprite de jogo.

## When to use

- `michi/select.jpg` is the approved box art
- You need the first south-facing idle, with painted volume and the same light

## Inputs

- **Text prompt** (below)
- **Image 1** — `michi/select.jpg`

Do pass the select. Translate it into a centered full-body game sprite. Do not copy the tavern.

## Prompt (copy & paste)

```text
Intended use: a single south-facing idle sprite frame for a top-down 2.5D action game on a flat 2D map. Final artwork should behave like one logical 256x256 in-game frame, delivered at 1024x1024 with readable painted volume at game scale.

Image 1 role: identity anchor. Preserve this exact character identity, palette, costume, silhouette, and top-left lighting direction. Translate the portrait into a centered full-body game sprite. Do not copy the tavern composition.

Subject:
- Michi, Feline Warrior, facing SOUTH directly toward the camera in 3/4 top-down game perspective.
- This is the canonical idle frame.
- Compact upright bipedal cat. Short cream and light-grey tabby fur. Darker tabby stripes on the forehead, cheeks, and ears. White muzzle, chest, and inner ears. Bright blue eyes. Pink nose. Calm feline face. A cream and grey tail. The head, pauldrons, breastplate, and skirt must all read when scaled down.
- Brown leather cuirass with crossing straps and buckles. Dark metal pauldrons. A segmented metal breastplate. A single fang pendant at the collar. Chainmail at the waist. A jagged brown leather skirt with metal studs. Leather bracers. Leather wraps on the lower legs. Bare feline paws on hands and feet. No boots, cloak, or hood.
- Standing still, feet planted, weight even. Both paws empty and relaxed at her sides. Alert, not walking and not lunging.
- No axe, no staff, no sword, no bow, and no held object.

Frame rules:
- One character only, centered.
- Full body visible, square 1024x1024 canvas.
- Visible body fits within the intended logical sprite box.
- Anchor/foot plant at bottom-center.
- Preserve idle readability, not an attack pose.
- Both feet visible, with no floor under them.

Style:
- pre-rendered 2.5D game sprite — painted fantasy illustration, not pixel art
- readable volume: soft shading on the tabby fur, leather, and metal
- one light only, from the top-left
- clean edges with controlled anti-aliasing — no muddy painterly blur
- character reads clearly when scaled down to 256x256

Background:
- solid flat chroma color #00FF00 (green)
- absolutely no ground shadow, floor plane, gradient, or environment
- no scenery, props, borders, UI, text, logo, or watermark

Avoid:
- the Gothic tavern, the rain, the window, and the violet neon sign from Image 1
- pixel art, SNES-style blocks, or chunky pixel clusters
- photorealistic fur strands or hyper-textured materials
- a weapon, a pink or magenta glow, runes, sparks, or an aura
- a walking stride, a crouch, or a raised fist
- dramatic camera angles or perspective distortion
- extra characters
```

## Recommended sizes

- Logical frame size = `256×256`
- Output size = `1024×1024` square

## Notes

- Attach `michi/select.jpg` as Image 1. The text alone will drift the armor.
- The approved select has a fang pendant at the collar. Keep that fang. It is costume, not a weapon.
- The green plate is `#00FF00`, flat, with no floor and no contact shadow. A shadow under the feet means the frame is rejected.
- Generate 2–4 variants and pick the one with the cleanest silhouette, the most stable foot baseline, and the closest match to the select.
- Both paws stay empty. The weapon is a later pass.

## Next step

Neutral anchor, only if this frame comes back with a weapon or a glow. Otherwise [03b — T-pose](03b-tpose.md).
