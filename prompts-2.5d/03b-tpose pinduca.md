# 03b — T-Pose (2.5D Real) — Pinduca

Two images, one pose. **A** locks the T-pose in the same world as the box art. **B** puts that same pose on flat green chroma. Before Meshy, remove the green so the upload is a transparent PNG. Meshy treats a green plate as part of the model.

Do this after the neutral anchor. The character is already identity-locked and has no magic orb.

## When to use

- Neutral anchor (step 03) is approved, or you are using the south anchor because the neutral file was not saved
- You need a modeling reference for Meshy before any walk video

## Approved inputs

- **Image 1 for prompt A** — `pinduca/pinduca-box1.png`. This is the only approved image with a readable face and the library. `pinduca-box2.png` was not used; it is in `old/pinduca/`.
- **Image 2 for prompt A** — neutral anchor if you have it. Otherwise `pinduca/2.5d/anchors/02-south-anchor.png`. Use it for full-body costume and the empty paws. Do not copy its top-down camera.
- **Image 1 for prompt B** — the approved result of prompt A

## A — T-pose with background

Output a wide frame, about 1536×1024, so both paws sit inside the picture with margin.

```text
Intended use: a full-body T-pose modeling reference of Pinduca, a Mystical Feline Mage, standing in her box-art world. This image locks the pose. A later step replaces the background with green chroma.

Image 1 role: face, palette, costume, and library. Preserve this character. Do not copy her portrait pose or the floating orb.
Image 2 role: full-body costume check. Match the robe, ruff, tail, and empty paws. Do not copy the top-down game camera or the sprite framing.

Camera:
- Eye level, looking straight at her face.
- Body turned only a few degrees, just enough for the tail to clear the robe.
- This is not a top-down view and not a 3/4 game sprite.

Subject:
- Pinduca, Mystical Feline Mage, in a clear T-pose.
- Arms extended straight out to the sides, parallel to the ground, with empty space between each arm and the shelves.
- Both paws fully inside the frame, open, empty, and unoccluded.
- Legs straight, feet slightly apart and grounded. Ears, robe hem, both feet, and the tail are fully inside the frame.
- Long-haired grey-and-white tabby, thick white ruff, sapphire-blue eyes, deep navy hooded wizard robe with the hood down on the shoulders, cyan rune trim on cuffs, front opening, and hem, blue waist sash, lighter blue V-neck underlayer.
- No staff, weapon, magic orb, glow burst, particles, or casting pose.

World/background:
- Dim antique Gothic library tower at night — tall dusty bookshelves, stacked leather-bound tomes, cobwebs, moonlight through a cracked arched leaded window.
- Shelves stay behind her. No book, cobweb, or window bar touches the outline of her arms, tail, or feet.

Style:
- painted fantasy illustration with readable volume
- single light source from the top-left
- clean edges, no muddy blur
- no text, logo, UI, watermark, or extra characters

Avoid:
- top-down game camera
- cropped hands, ears, feet, or tail
- arms touching the left or right edge
- pixel art or photoreal fur strands
- redesigning the costume or adding props
```

## B — T-pose on chroma

Generate this only after A is approved. This is a background swap. Reject it if the face, arms, or robe changed.

```text
Intended use: the same approved T-pose prepared for background removal. One full-body character on a flat chroma background. Wide frame, about 1536×1024, character centered, both paws well inside the canvas.

Image 1 role: pose and identity lock. Preserve this exact T-pose, face, outfit, palette, proportions, silhouette, painted style, and top-left light. Replace only the background.

Subject:
- Same Pinduca, same T-pose, same eye-level camera, same few degrees of turn.
- Full body in frame, including both paws, ears, feet, and tail. Nothing cropped.
- No orb, particles, weapon, or casting glow. Cyan rune trim on the robe stays; it is costume, not an effect.
- Hard edge between the character and the green. No green spill on fur, robe, rune glow, or tail.

Background:
- solid flat chroma color #00FF00
- absolutely no ground shadow, floor plane, gradient, scenery, border, text, logo, or watermark

Avoid:
- changing the pose, scale, costume, or identity
- regenerating a new face or a new arm position
- top-down game framing
- pixel art or photoreal fur
```

## Before Meshy

Remove `#00FF00` from the approved B and upload the transparent PNG. A green rectangle behind her becomes a card in the mesh, and green fringe bakes into the fur and the rune trim.

## Notes from the Pinduca run

- Prompt A is the pose lock. Prompt B only swaps the background.
- Box art supplies the face. The anchor supplies the body without the orb. Neither image supplies this camera.
- Keep a margin around both paws. A square 1024 crop cuts a T-pose at the wrists.
- If the arms bend, the tail hides behind the robe, or a foot is cut off, reroll A before doing B.
- Chroma stays `#00FF00`, same as the south anchor.

## Next step

→ [04 — Walk video](04-walk-video%20pinduca.md), after Meshy and the saved Flow character.
