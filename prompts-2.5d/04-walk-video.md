# 04 — Walk video, west only

The walk prompt below is the one that shipped: strict left profile, small steps, green chroma, no floor. Do not switch it to a 3/4 view, a grey background, or a walk that starts from a T-pose.

Idle is a second clip with the same camera and the same green void. Mixing a held idle into the walk breaks the seamless loop.

## Walk (copy & paste)

```text
Full-body character asset for video game 2D sprite sheet extraction. {CHARACTER_NAME} walks in place facing completely sideways to the left in a strict side profile view (perfil lateral), looking directly to the left instead of toward the camera. Frame one is already this left profile. Do not show a T-pose. Do not turn from the front.

{CORE_IDENTITY}
{COSTUME_AND_COLOR_PALETTE}

Walks with small steps, arms down at the sides with an extremely subtle, soft sway, almost still, no exaggerated movement. Floating in mid-air void with absolutely no floor, no ground plane, no floor surface. Solid flat uniform chromakey green screen background (#00FF00) filling the entire frame. Completely flat unlit environment, zero ground shadows, zero floor contact shadows, zero ambient occlusion. Perfectly centered with generous padding around ears, tail, and paws. Seamless looping in-place walk cycle.
```

## Idle (copy & paste, same plate)

```text
Full-body character asset for video game 2D sprite sheet extraction. {CHARACTER_NAME} stands idle, facing completely sideways to the left in a strict side profile view (perfil lateral), looking directly to the left instead of toward the camera. Frame one is already this left profile. Do not show a T-pose.

{CORE_IDENTITY}
{COSTUME_AND_COLOR_PALETTE}

Both feet planted, not stepping. Arms down at the sides, almost still. Only a tiny breath. Floating in mid-air void with absolutely no floor, no ground plane, no floor surface. Solid flat uniform chromakey green screen background (#00FF00) filling the entire frame. Completely flat unlit environment, zero ground shadows, zero floor contact shadows, zero ambient occlusion. Perfectly centered with generous padding around ears, tail, and paws. Hold this pose. No walk cycle.
```

## After the videos

Export both clips. Idle frames come from the hold. Walk frames come from the loop. Build one sheet in Sprite Smithy and mirror it for the right-facing side.

Reject a clip that opens on a T-pose, turns toward the camera, or shows any oval under the feet.
