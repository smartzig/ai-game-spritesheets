# 03 — Neutral Anchor Reset (2.5D Real)

If your south anchor came out with a baked-in dynamic effect (fireball in hand, drawn weapon, casting glow), regenerate it neutral. **Anchors are boring on purpose.** Effects belong in the attack sheet only.

Same rule as the [pixel pipeline](../old/pixel-tutorial/prompts/03-neutral-anchor.md) — only the style inputs change.

## When to use

- Your south anchor has a magic effect, charged weapon, or active pose
- You realize the effect would persist into idle/walk frames downstream

## Inputs

- **Text prompt** (template below)
- **Image 1** — your existing south anchor (identity reference)
- **Image 2** (optional) — approved box art, if the anchor drifted too far from original identity

## Why one or two image inputs

Using only the existing anchor preserves scale and painted style. Add box art as **Image 2** only if identity drifted (face, palette, or proportions changed too much from step 02).

## Prompt template

```text
Intended use: corrected reusable SOUTH-facing neutral idle anchor sprite for {CHARACTER_NAME}, a {ARCHETYPE} character in a top-down 2.5D game on a flat 2D map.

Image 1 role: identity anchor. Preserve this exact character identity, detail level, face, outfit, palette, prop, proportions, silhouette, painted 2.5D style, and sprite scale.
Image 2 role (if provided): original box-art identity. Use only to recover face/palette/proportions if Image 1 drifted. Do not copy the portrait composition.

Primary request:
Create {N} candidate variants of the same SOUTH-facing neutral idle anchor.
The only intended design correction from Image 1 is removing {DYNAMIC_EFFECT}.

Subject:
- {CHARACTER_NAME}, {ARCHETYPE}.
- Facing SOUTH, directly toward the camera.
- Same silhouette, outfit, palette, prop, face readability, and body scale as Image 1.
- {DYNAMIC_EFFECT_HAND_OR_BODY_PART} should be neutral and empty/resting naturally.

Preserve from Image 1:
- same face readability
- same silhouette and proportions
- same costume colors and material treatment
- same prop size/detail
- same centered composition
- same painted 2.5D pre-rendered style
- same top-left light source

Change from Image 1:
- remove {DYNAMIC_EFFECT}
- remove glow, particles, smoke, aura, projectile, and charged action pose
- make the pose read as neutral idle

Background:
- solid flat chroma background #00FF00 outside the character
- no gradients, noise, ground shadow, scenery, text, border, or UI

Avoid:
- redesigning the character
- simplifying key identity details
- changing scale or silhouette
- adding action effects
- pixel art or flat SNES-style rendering
```

## Notes

- Generating 4 variants and picking the cleanest one is faster than re-rolling singles.
- If hands/paws still look "charged" after reset, specify exactly which body part must be empty in `{DYNAMIC_EFFECT_HAND_OR_BODY_PART}`.

## Next step

→ [03b — T-Pose](03b-tpose.md)
