# 05 — Monster (still + animation)

Two prompts. In the first, replace one sentence: the identity. In the second, attach the approved still and replace one sentence: the motion.

The Purrfect Storm alley stays in these notes. It does not go into the prompt. Dumpsters, cars, and neon signs make the generator draw the street. The monster sentence describes only the creature: an animal, a piece of trash, or a piece of junk a stray cat would meet in that alley, with the energy of a gig spinning out of control.

## What you change

| Field | Where it goes | What to write |
|---|---|---|
| `{MONSTER}` | Still, after `The character is:` | One sentence: what it is, body and colors, one detail that reads small, attitude and silhouette |
| `{MOTION}` | Video or spritesheet, after `The motion is:` | One in-place motion sentence. The body does not travel across the frame |

Example `{MONSTER}`:

```text
a plump street pigeon with a puffed chest, messy gray feathers, an iridescent neck, stubby legs, and an annoyed look, compact and wide
```

## 1 — Still

One paste block. It opens with the background so the generator cannot treat the plate as optional. No input image.

Paste this into Meshy and into the image generator. There is no separate character-only prompt: that version is what produced the dark alley and the trash pedestal.

```text
Solid flat uniform chromakey green screen background (#00FF00) filling the entire image edge to edge. Every background pixel is the same flat unlit green. No gradient, no blur, no bokeh, no vignette, no street, no room, no dark backdrop. One single view, not a turnaround, not two panels.

One stylized 3D game character floating in empty space. Full body, hand-painted soft shading, light on the character only from the upper left, chunky silhouette readable at small size. Small neon magenta and cyan marks on the body only. Neutral standing pose, facing three-quarter toward the camera, feet visible and fully inside the frame, centered, with padding around the silhouette. Absolutely no floor, no ground plane, no display base, no pedestal, no podium, no rubble pile, no contact shadow, no text. The character is: {MONSTER}
```

Reject the still if the backdrop is dark, blurred, or scenic, if the character stands on a base, or if the feet are cropped. Cyan and magenta on the body are costume. Green on the body spills into the cutout.

### Body only

Use this still when the game will move the monster in code: bob, squash, tilt, pulse. One picture. No spritesheet. The body is a single closed mass. Legs, feet, wings, arms, and a separate jaw give the generator pieces the code cannot bend.

```text
Solid flat uniform chromakey green screen background (#00FF00) filling the entire image edge to edge. Every background pixel is the same flat unlit green. No gradient, no blur, no bokeh, no vignette, no street, no room, no dark backdrop. One single view, not a turnaround, not two panels.

One stylized 3D game character floating in empty space. One single closed body, hand-painted soft shading, light on the character only from the upper left, chunky silhouette readable at small size. Small neon magenta and cyan marks on the body only. Facing three-quarter toward the camera, centered, with padding around the silhouette. No legs, no feet, no wings, no arms, no hands, no tail, no separate jaw. The bottom of the body is a smooth rounded hull. Eyes and markings are painted on the body, not separate moving parts. Absolutely no floor, no ground plane, no display base, no pedestal, no podium, no rubble pile, no contact shadow, no text. The character is: {MONSTER}
```

`{MONSTER}` still describes the creature, and it does not mention legs or wings. Example: `a plump street pigeon compressed into one round body, messy gray feathers, an iridescent neck, a short beak, and an annoyed look, compact and wide`

Reject the still if any leg, foot, wing, or arm appears, even a stub.

## 2 — Animation

The reference image locks the character only. A black, dark, or scenic backdrop in that image is replaced. Every frame is flat `#00FF00`. Camera, crop, and upper-left light stay fixed. The pose changes. Six copies of the still are a failed sheet.

Many of these monsters share the screen, so one cycle stays short. Six distinct poses, played over about two seconds. Sixteen frames is the ceiling, not the goal. The feet return to the same invisible ground line. That line is not a drawn floor.

If the video tool has a duration control, set it to 2 seconds. The prompt asks for one cycle and six poses. A long clip still has to be cut down to those poses on export.

### Video

```text
Solid flat uniform chromakey green screen background (#00FF00) filling the entire frame edge to edge in every moment. Flat unlit green only. Not black, not dark, and not a copy of the reference backdrop. No street, no blur, no base, no pedestal, no floor, no contact shadow. Use the reference image for the character only. Keep the same design, colors, proportions, and painted style. The pose must change. Do not hold the reference pose for the whole clip. Three-quarter view, full body in frame the whole time. The chest keeps the same three-quarter angle in every moment, matching the reference. Camera locked, no zoom, no pan, no cut, no turn to side profile. Light on the character only, from the upper left. Feet stay on the same invisible ground line in every moment. One complete cycle only, about two seconds, no second repeat. Exactly six distinct poses, even timing, no extra in-between frames. Sixteen frames is the hard maximum. Seamless loop, no travel across the frame. The motion is: {MOTION}
```

### Spritesheet

Use this when the tool generates the strip directly, instead of a video.

```text
Solid flat uniform chromakey green screen background (#00FF00) filling every cell edge to edge. Flat unlit green only. Not white, not black, not dark, not transparent, not a copy of the reference backdrop. No street, no blur, no base, no pedestal, no floor, no contact shadow. No text, no captions, no pose numbers, no words. Spritesheet of the reference character only. Keep the same design, colors, proportions, and painted style. Exactly six equal square cells in one single horizontal row. Not two rows. Not a pose chart. One complete cycle, no extra cells. Full body in every cell. The chest faces the same three-quarter angle in every cell, matching the reference. The camera does not turn. Do not rotate the body into a side profile. Only the neck, head, and feet move. Neighboring cells show a different head position and a different foot position, obvious when the character is small. Feet on the same invisible ground line in every cell. Crop and upper-left light on the character identical across frames. Seamless loop, no travel across the cell. The motion is: {MOTION}
```

### Ready motions

Replace `{MOTION}` with one of these, or write another in the same shape: what the body does, on which poses, and that it stays in place.

Hop:

```text
a small hop in place, body up on poses 2 and 5, feet back on the ground line
```

Crawl:

```text
a low crawl in place, belly close to the ground line, legs cycling, body stays in the cell
```

Hover:

```text
a gentle hover bob, body rises and falls slightly, no sideways drift
```

Fly:

```text
an in-place hover flight with big readable changes. The chest keeps the same three-quarter angle in every pose. Do not turn the body to side profile. The whole body rises and falls. Pose 1: body low. Pose 2: body lifted high. Pose 3: body still high, starting to descend. Pose 4: body low again. Pose 5: body lifted high. Pose 6: body descends back to the low pose, matching pose 1. The body travels a long way up and down. A slight bob is not enough. The body stays centered in the cell, no sideways drift
```

Charge:

```text
an in-place belly charge with a huge silhouette change. Every cell uses the same three-quarter camera. A side view in any cell is wrong. Do not curl into a ball. The paws, the tongue, and the tail are not the animation. Pose 1: upright oval, belly settled, crown level, tail hanging. Pose 2: body squashed shorter and wider, crown tipped back. Pose 3: spine tipped far forward, belly shoved past the feet, crown pointing forward, tail straight up. Pose 4: the same forward wedge, held. Pose 1 is an upright oval and pose 4 is a forward wedge. If those two silhouettes match, the pose is wrong. Pose 5: still tipped forward, starting to rise. Pose 6: upright oval again, matching pose 1. The body stays centered in the cell, feet on the same invisible ground line, no sideways travel
```

On a charge sheet, the whole body tips. A nod, a tail curl, or a side view is a failed sheet. If a six-cell strip already exists and the lean is missing, edit that strip. Do not generate a new rat.

### Edit this sheet

Use this when the strip is already one green row of six cells and the motion is too small. Attach that image. This pass changes the poses. It does not redraw the character.

```text
Edit the attached spritesheet. Keep this same character, colors, proportions, painted style, three-quarter angle, crop, and upper-left light. Keep exactly six equal cells in one horizontal row on flat #00FF00. No white, no black, no text, no second row. Do not turn the body to side profile. The chest stays aimed the same way in every cell. Change only the neck, head, and feet, with a big readable difference between neighbors. Pose 1: head pulled back against the body, left foot lifted. Pose 2: neck and head thrust far forward, both feet down. Pose 3: head still forward, right foot lifted. Pose 4: head pulled back against the body, right foot lifted. Pose 5: neck and head thrust far forward, both feet down. Pose 6: head starts back and the left foot lifts, matching pose 1. A slight head tilt is not enough. The body stays centered in each cell, feet returning to the same invisible ground line.
```

## After the clip

Export the frames and cut the `#00FF00` with `.cursor/skills/cut-chroma-frames/`. Keep the six poses. If the clip came back longer, drop it to at most sixteen frames before it becomes a spritesheet. In game, that loop plays in about two seconds. A clip with a contact shadow or a drawn floor is rejected. The script does not invent a clean plate the video failed to draw.
