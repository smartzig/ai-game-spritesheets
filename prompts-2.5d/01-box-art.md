# 01 — Box Art (2.5D Real)

Generate the high-resolution identity image for your character. In the **2.5D Real** pipeline, box art is **more central** than in pixel art — it becomes the primary identity reference for the south anchor (step 02).

## When to use

- You're starting a new character from scratch
- You want a visual anchor for color palette, silhouette, prop, lighting, and personality
- You'll reuse it as **Image 1** in the south anchor step

## Inputs

- Text prompt only (no image references at this stage)
- Tool: GPT Image 2.0 / Nano Banana 2 / your favorite image model

## Prompt template

```text
Create a high-resolution character box-art portrait for {CHARACTER_NAME}, a {CHARACTER_ARCHETYPE}, for a top-down 2.5D battle game with a flat 2D map.

Format:
- 1696x2528 PNG
- 2:3 portrait, the same canvas as `pinduca/pinduca-box1.png`
- full-body or near full-body 3/4 hero composition
- painted illustration with strong silhouette and readable volume — must translate into pre-rendered 2.5D game sprites

Character:
- {CORE_IDENTITY}
- {COSTUME_AND_COLOR_PALETTE}
- {SIGNATURE_PROP}
- {PERSONALITY_OR_POSE}

Lighting and volume:
- single consistent light source from top-left
- soft but readable shading on face, costume folds, and props
- grounded feet — character reads as standing on a flat surface
- no extreme perspective distortion

World/background:
- {CHARACTER_SPECIFIC_BIOME}
- same world language as the rest of the roster
- background supports the character, but does not overpower them

Avoid:
- text, logos, UI, watermark
- symbols/runes/glyphs unless explicitly part of the design
- background motifs that belong to another character
- pure pixel art or SNES-style blockiness
- photorealistic skin pores or hyper-detailed textures
```

## Notes

- Box art sets **palette, silhouette, and lighting direction** for every downstream asset.
- Keep baked-in magic effects minimal here — dynamic VFX belong in the attack sheet (step 06), same as the pixel pipeline.
- If runes or symbols drift into unwanted places, do a second pass explicitly removing them (same lesson as the wizard run).

## Next step

→ [02 — South Anchor](02-south-anchor.md)
