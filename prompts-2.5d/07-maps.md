# 07 — Mapas (chão da arena)

O mapa 1 já existe: `game/assets/maps/map_1/map-alley.png`, 2560×1440. Estes cinco são o baldio, a caixa de areia, a casa, o cafezal e o hospital. Cada um é um PNG só, o chão inteiro da arena.

A colisão do jogo já é um anel na borda (`BorderCollisions` em `game_level.tscn`). O desenho entra nesse anel. O meio fica chão liso. Assim o gato para na parede pintada e não precisa de bloqueio novo no meio do mapa.

## Formato

| | |
|---|---|
| Arquivo | um PNG, 16:9 |
| Pixels | **2560×1440** |
| Enquadramento | de cima, a arena inteira, sangria até a borda da imagem |
| Luz | uma só, vinda do alto à esquerda |
| Pintura | a mesma família do beco: volume pintado, magenta e ciano como acento |

Se a ferramenta não aceitar 2560×1440, peça o 16:9 maior que ela entregar, sem tarja e sem margem. O jogo estica o PNG para 2560×1440. Um 16:9 nativo evita o estica torto.

Recusa se o tamanho não for 16:9, se a rua continuar para fora do quadro, se aparecer gato, monstro, texto ou objeto no meio com volume (carro, caixote, móvel, árvore, pedra, lata em pé).

## Onde a parede entra

A parede ocupa só a faixa que o jogo já bloqueia. O chão é o retângulo de dentro. As quatro faixas se encontram nos cantos e fecham a arena. Não há portão, boca de rua nem vão.

| Faixa | Pixels no 2560×1440 | Fatia do quadro |
|---|---|---|
| Topo | altura 290, de y 0 a 290 | 20% da altura |
| Baixo | altura 333, de y 1107 a 1440 | 23% da altura |
| Esquerda | largura 140, de x 0 a 140 | 5,5% da largura |
| Direita | largura 166, de x 2394 a 2560 | 6,5% da largura |
| Chão | x 140–2394, y 290–1107 | o resto |

Topo e baixo são grossos, como as lojas do beco. Esquerda e direita são finas: a mesma parede dobrando a esquina, contínua, sem fresta. Material sólido de ponta a ponta (tijolo, metal, vidro, cerca, cerca-viva). Uma faixa fina lê como parede quando não tem buraco.

O chão é tinta chapada: rachadura, mancha, rejunte, areia, linha pintada. Nada ali tem altura. O gato passa por cima.

## Chapa

Copie o bloco. Troque `{MAP}` e `{BORDER}` e `{FLOOR}`.

```text
One single top-down arena ground for a 2.5D game, the whole map in one frame. 2560x1440 PNG, exact 16:9, full bleed, edge to edge. No letterbox, no margin, no UI, no watermark.

High overhead view, the same camera as a neon alley arena: the floor is seen from above, and the perimeter walls show their face. One light from the upper left. Hand-painted volume, soft shading, readable at game scale. Magenta and cyan only as small accents. No pixel art, no photo, no horizon, no vanishing street.

The arena is closed on all four sides. Solid scenery touches every edge of the image and meets at the four corners. No gate, no doorway opening, no road, alley, or path leaving the frame.

Wall bands, and nothing else has volume:
- Top band: the top 20% of the height, full width. {BORDER}
- Bottom band: the bottom 23% of the height, full width. Same closed wall.
- Left band: the left 5.5% of the width, full height. The same wall turning the corner, thin and unbroken.
- Right band: the right 6.5% of the width, full height. The same wall turning the corner, thin and unbroken.

Inner floor, the open rectangle inside those bands: {FLOOR} Flat paint only. Cracks, stains, grout, and painted marks sit in the surface. No car, crate, dumpster, rock, tree, bush, furniture, table, counter, or upright litter anywhere on the floor. A cat walks the whole inner rectangle without bumping into anything.

No characters, no creatures, no text, no letters, no readable signs.
```

## Terreno Baldio

Mapa 2. Lote vazio do Zigo. Arquivo: `game/assets/maps/map_2/map-lot.png`.

`{BORDER}`

```text
a continuous rusted corrugated-metal fence and scrap-metal hoarding, chain-link over concrete, night, a few cyan and magenta neon scraps on the metal, the fence is the wall itself
```

`{FLOOR}`

```text
packed dirt and cracked asphalt of an empty lot at night, oil stains, flat dead-grass patches, flattened litter painted into the ground
```

## Caixa de Areia

Mapa 3. O playground da Michi, visto como uma caixa de areia gigante. Arquivo: `game/assets/maps/map_3/map-sandbox.png`.

`{BORDER}`

```text
the wooden plank walls of a giant sandbox, warm painted boards with a low playground fence along the top of the wood, daylight, the boards are the wall itself
```

`{FLOOR}`

```text
flat play sand in daylight, soft ripples, a few painted paw prints, no toys sitting on the sand
```

## Casa

Mapa 4. Uma sala do apartamento, cercada pelas quatro paredes. Arquivo: `game/assets/maps/map_4/map-apartment.png`.

`{BORDER}`

```text
the four walls of one apartment room, wallpaper, baseboard, and closed doors that read as solid wall, warm indoor light, a small magenta neon on one wall
```

`{FLOOR}`

```text
empty hardwood floor, boards running across the room, a flat worn oval in the varnish, no rug with thickness and no furniture
```

## Cafezal

Mapa 5. Clareira fechada. Os pés de café são a cerca, não fileiras no meio. Arquivo: `game/assets/maps/map_5/map-plantation.png`.

`{BORDER}`

```text
a dense coffee-tree hedge on a low stone terrace wall, sunlit green leaves and red berries, the hedge is the wall itself and does not step into the clearing
```

`{FLOOR}`

```text
flat red plantation soil in a sunlit clearing, painted leaf shadows, a few flat fallen leaves in the dirt
```

## Hospital

Mapa 6. Sala de exame vazia. Armários e paredes clínicas ficam no anel. Arquivo: `game/assets/maps/map_6/map-clinic.png`.

`{BORDER}`

```text
veterinary clinic walls, cold tile and stainless cabinet faces, a shut exam-room door, harsh white light with a thin cyan reflection, the cabinets are the wall itself
```

`{FLOOR}`

```text
empty pale clinic tile, grout grid, one flat scuff, no table, no trolley, no cage
```
