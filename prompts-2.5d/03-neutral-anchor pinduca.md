# 03 — Neutral Anchor Reset (2.5D Real) — Pinduca

If your south anchor came out with a baked-in dynamic effect (floating orb, casting glow, energy wisps), regenerate it neutral. **Anchors are boring on purpose.** Effects belong in the attack sheet only.

Same rule as the [pixel pipeline](../old/pixel-tutorial/prompts/03-neutral-anchor%20pinduca.md) — only the style inputs change.

## When to use

- Your south anchor has a magic orb, charged casting pose, or active glow
- You realize the effect would persist into idle/walk frames downstream

## Inputs

- **Text prompt** (template below)
- **Image 1** — your existing south anchor (identity reference)
- **Image 2** (optional) — approved box art from step 01, if the anchor drifted too far from original identity

## Why one or two image inputs

Using only the existing anchor preserves scale and painted 2.5D style. Add box art as **Image 2** only if identity drifted (face, palette, or proportions changed too much from step 02).

## Prompt (copy & paste)

```text
Intended use: corrected reusable SOUTH-facing neutral idle anchor sprite for Pinduca, a Mystical Feline Mage character in a top-down 2.5D game on a flat 2D map.

Image 1 role: identity anchor. Preserve this exact character identity, detail level, face, outfit, palette, prop, proportions, silhouette, painted 2.5D pre-rendered style, and sprite scale.
Image 2 role (if provided): original box-art identity. Use only to recover face/palette/proportions if Image 1 drifted. Do not copy the portrait composition.

Primary request:
Create 4 candidate variants of the same SOUTH-facing neutral idle anchor.
The only intended design correction from Image 1 is removing the floating cyan-violet magic orb, casting glow, energy wisps, and charged casting pose.

Subject:
- Pinduca, Mystical Feline Mage.
- Facing SOUTH, directly toward the camera.
- Same silhouette, outfit, palette, face readability, and body scale as Image 1.
- Her open casting paw should be neutral and empty/resting naturally at her side or lightly raised without any orb.

Preserve from Image 1:
- same face readability (grey-white tabby, sapphire eyes, white ruff)
- same silhouette and proportions (fluffy head, long robe, bushy ringed tail)
- same costume colors (deep navy robe, cyan rune trim, blue sash)
- same prop size/detail (no physical weapon — keep paws empty)
- same centered composition
- same painted 2.5D pre-rendered style with top-left light source

Change from Image 1:
- remove the floating cyan-violet magic orb, casting glow, energy wisps, and charged casting pose
- remove glow, particles, smoke, aura, projectile, and charged action pose
- make the pose read as neutral idle

Background:
- solid flat chroma background #00FF00 outside the character
- no gradients, noise, ground shadow, scenery, text, border, or UI

Avoid:
- redesigning the character
- simplifying key identity details (keep cyan robe rune trim)
- changing scale or silhouette
- adding action effects
- pixel art or flat SNES-style rendering
```

## Notes from the Pinduca run

- If south came back with a cyan-violet orb in the casting paw, strip it here — it would persist across all walk frames.
- Keep the embroidered cyan rune trim on the robe; that is **costume identity**, not a dynamic effect.
- Generating 4 variants and picking the cleanest one was faster than re-rolling singles.

## Next step

→ [03b — T-Pose](03b-tpose%20pinduca.md)
