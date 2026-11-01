# 03b — T-Pose (2.5D Real)

Two images, one pose. **A** locks the T-pose in the same world as the box art. **B** puts that pose on flat green chroma. Meshy receives the transparent PNG made from **B**. There is no separate Meshy text prompt.

## Inputs

- **Image 1 for prompt A** — approved box art from step 01
- **Image 2 for prompt A** — approved neutral anchor from step 03
- **Image 1 for prompt B** — the approved result of prompt A

Use the same `{CORE_IDENTITY}` and `{COSTUME_AND_COLOR_PALETTE}` as steps 01–03.

## A — T-pose with background

Wide frame, about 1536×1024, so both hands sit inside the picture with margin.

```text
Intended use: a full-body T-pose modeling reference of {CHARACTER_NAME}, a {CHARACTER_ARCHETYPE}, standing in the box-art world. This image locks the pose. A later step replaces the background with green chroma.

Image 1 role: face, palette, costume, and world. Preserve this character. Do not copy the portrait pose or any held effect.
Image 2 role: full-body costume check. Match the outfit and the empty {EMPTY_LIMB}. Do not copy the top-down game camera or the sprite framing.

Camera:
- Eye level, looking straight at the face.
- Body turned only a few degrees, just enough for a tail, cape, or back accessory to clear the body.
- This is not a top-down view and not a 3/4 game sprite.

Subject:
- {CHARACTER_NAME}, {CHARACTER_ARCHETYPE}, in a clear T-pose.
- {CORE_IDENTITY}
- {COSTUME_AND_COLOR_PALETTE}
- Arms extended straight out to the sides, parallel to the ground, with empty space between each arm and the background.
- Both hands fully inside the frame, open, empty, and unoccluded.
- Legs straight, feet slightly apart and grounded. Ears or head, costume hem, both feet, and any tail are fully inside the frame.
- No staff, weapon, magic orb, glow burst, particles, or casting pose.

World/background:
- {CHARACTER_SPECIFIC_BIOME}
- Scenery stays behind the character. Nothing touches the outline of the arms, feet, or tail.

Style:
- painted fantasy illustration with readable volume
- single light source from the top-left
- clean edges, no muddy blur
- no text, logo, UI, watermark, or extra characters

Avoid:
- top-down game camera
- cropped hands, ears, feet, or tail
- arms touching the left or right edge
- pixel art or photoreal texture
- redesigning the costume or adding props
```

## B — T-pose on chroma

Generate this only after A is approved. This is a background swap. Reject it if the face, arms, or costume changed.

```text
Intended use: the same approved T-pose prepared for background removal. One full-body character on a flat chroma background. Wide frame, about 1536×1024, character centered, both hands well inside the canvas.

Image 1 role: pose and identity lock. Preserve this exact T-pose, face, outfit, palette, proportions, silhouette, painted style, and top-left light. Replace only the background.

Subject:
- Same {CHARACTER_NAME}, same T-pose, same eye-level camera, same few degrees of turn.
- {CORE_IDENTITY}
- {COSTUME_AND_COLOR_PALETTE}
- Full body in frame. Nothing cropped.
- No orb, particles, weapon, or casting glow. Costume trim stays; it is costume, not an effect.
- Hard edge between the character and the green. No green spill on the character.

Background:
- solid flat chroma color #00FF00
- absolutely no ground shadow, floor plane, gradient, scenery, border, text, logo, or watermark

Avoid:
- changing the pose, scale, costume, or identity
- regenerating a new face or a new arm position
- top-down game framing
- pixel art or photoreal texture
```

## Meshy

Remove `#00FF00` from the approved B and upload the transparent PNG. A green rectangle behind the character becomes a card in the mesh.

Meshy does not get a character-design prompt. The image is the character. Download the model and the view prints. Those prints become the saved character in Google Flow for the walk video.

## Next step

→ [04 — Walk video](04-walk-video.md)
