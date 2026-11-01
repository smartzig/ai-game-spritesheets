# 06 — Itens (categorias)

Um PNG por item. A chapa abaixo vale para todos. O que este arquivo guarda é a **categoria**: a frase da silhueta e do material. A personalidade (efeitos, cores, desenhos) entra no espaço de cada item, antes de gerar.

A mesma imagem vai para o jogo e para a documentação. O arquivo nasce em 1024×1024.

## Chapa

Copie o bloco. Troque `{CATEGORY}` pela frase do item. Preencha a personalidade no próprio bloco, ou deixe as cinco linhas como estão neste arquivo e copie de lá.

```text
Solid flat uniform chromakey green screen background (#00FF00) filling the entire image edge to edge. Every background pixel is the same flat unlit green. No gradient, no blur, no bokeh, no vignette, no street, no room, no dark backdrop. One single view, not a turnaround, not two panels.

Square 1024x1024 PNG, 1:1. One game item icon, centered, large in the frame, with a slim even margin. Every tip stays inside the canvas. The same picture is the in-game icon and the documentation image.

One stylized 2.5D game prop floating in empty space. Hand-painted soft shading, light on the object only from the upper left, chunky silhouette readable at small size. Three-quarter view toward the camera, matching the game characters. No cat, no mannequin, no hand, no head inside it.

Category: {CATEGORY}

Personality:
- Colors: {COLORS}
- Effect A: {EFFECT_A}
- Effect B: {EFFECT_B}
- Effect C: {EFFECT_C}
- Drawings: {DRAWINGS}

Painted effects sit on the surface. No outer glow, no particles, no aura, no sparkles in the air. Absolutely no floor, no ground plane, no display base, no pedestal, no contact shadow, no text, no letters, no logo. No green paint anywhere on the object.
```

Recusa se o fundo não for o verde chapado, se aparecer chão, sombra ou pedestal, se o objeto ficar de perfil ou minúsculo no quadro, se voltar pixel art com contorno preto, ou se tiver verde pintado nele. Magenta e ciano na superfície são figurino.

## Como acrescentar o próximo

Duplique o bloco do item. Preencha nome, código, arquivo e a frase de categoria. A personalidade fica vazia até você colar os efeitos. Itens da mesma família usam a mesma câmera; a frase de categoria é o que muda o tamanho e o material.

Um único (Whisker Edge, The Grandpurr) reaproveita a categoria da base e troca só a personalidade.

## Espadas

Diagonal, cabo embaixo à esquerda, ponta em cima à direita, três quartos, a mesma câmera nas duas. O fio pega a luz de cima à esquerda. A curta ocupa menos comprimento que a longa, no mesmo quadro de 1024.

### Short Sword

Ícone aprovado. O sprite que a arma usa dentro da wave continua o pixel antigo.

| | |
|---|---|
| Código | `shortsword` |
| Mãos | 1 |
| Ícone (HUD e wiki) | `game/assets/weapons/weapon_short_sword_icon.png` |
| Wave | `game/assets/weapons/weapon_short_sword.png` |

Categoria:

```text
a short one-hand iron sword a cat would swing, broad short blade, thick crossguard, wrapped grip, paw pommel, diagonal with the hilt at the lower left and the tip at the upper right, compact chunky silhouette
```

Personalidade:

- Colors: cold iron gray blade, brass and dark iron on the guard, brown wrapped grip
- Effect A: cat ears cut into the blade tip
- Effect B: one small neon magenta dash on the blade
- Effect C: a paw-shaped pommel and a small cat face on the guard
- Drawings: brass scrollwork, scratches on the iron

### Heavy Fang Sword

Único. Mesma câmera diagonal da Short Sword. O sprite da wave continua o pixel antigo.

| | |
|---|---|
| Código | `heavy_fang_sword` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_heavy_fang_sword_icon.png` |
| Wave | `game/assets/weapons/weapon_heavy_fang_sword.png` |

Categoria:

```text
a heavy one-hand iron sword a cat would swing, broad chipped blade, thick reinforced guard, wrapped grip, hex pommel, diagonal with the hilt at the lower left and the tip at the upper right, compact chunky silhouette
```

Personalidade:

- Colors: cold iron gray blade, brass trim on the fuller, dark wrapped grip
- Effect A: cat ears and short spikes along the blade tip
- Effect B: one small neon magenta dash on the blade
- Effect C: a small cat face stamped on the guard
- Drawings: angular marks carved in the fuller, chips along the edge

### Swift Claw Sword

Único. Mesma câmera diagonal da Short Sword. O sprite da wave continua o pixel antigo.

| | |
|---|---|
| Código | `swift_claw_sword` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_swift_claw_sword_icon.png` |
| Wave | `game/assets/weapons/weapon_swift_claw_sword.png` |

Categoria:

```text
a curved one-hand iron saber a cat would swing, long sweeping blade, open knuckle guard, wrapped grip, diagonal with the hilt at the lower left and the tip at the upper right, tall chunky silhouette
```

Personalidade:

- Colors: cold iron gray blade, brass claw guard, dark wrapped grip
- Effect A: a brass knuckle guard shaped like overlapping claws, with a gap in the middle
- Effect B: one small neon magenta dash on the blade
- Effect C: a notch cut out of the back of the blade near the tip
- Drawings: scratches on the iron, a wrapped cord on the grip

### Whisker Edge

Único sobre a Short Sword. Mesma câmera diagonal. Só o ícone; a wave da Short Sword não muda.

| | |
|---|---|
| Código | `whisker_edge` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_whisker_edge_icon.png` |

Categoria:

```text
a one-hand iron sword a cat would swing, long slender blade with open windows down the fuller, winged guard, wrapped grip, pointed pommel, diagonal with the hilt at the lower left and the tip at the upper right, tall chunky silhouette
```

Personalidade:

- Colors: cold iron gray blade, brass wings, dark wrapped grip, gold collar on the pommel
- Effect A: brass wings around a small iron cat head on the guard
- Effect B: one small neon magenta dash on the blade
- Effect C: a pointed pommel with a gold ring
- Drawings: two open windows cut through the blade, a wrapped cord on the grip

### Alley Slicer

Único sobre a Long Sword. Cabo em cima à direita, ponta embaixo à esquerda, a mesma câmera da Long Sword. Só o ícone; a wave da Long Sword não muda.

| | |
|---|---|
| Código | `alley_slicer` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_alley_slicer_icon.png` |

Categoria:

```text
a heavy two-hand iron sword a cat would swing with both paws, long broad blade, spiked guard, wrapped grip, crowned pommel, diagonal with the hilt at the upper right and the tip at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: cold dark iron blade, brown wrapped grip
- Effect A: a cat head on the guard, with ear spikes on either side
- Effect B: one small neon magenta dash on the blade
- Effect C: a crowned pommel with three spikes
- Drawings: a row of rivets down the blade, a layered fuller

### Long Sword

Ícone aprovado. O sprite que a arma usa dentro da wave continua o pixel antigo. Nesta arte o cabo ficou em cima à direita e a ponta embaixo à esquerda.

| | |
|---|---|
| Código | `longsword` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_long_sword_icon.png` |
| Wave | `game/assets/weapons/weapon_long_sword.png` |

Categoria:

```text
a long two-hand iron sword a cat would swing with both paws, long broad blade, wide thick crossguard, long wrapped grip, hex pommel, diagonal with the hilt at the upper right and the tip at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: cold iron gray blade, dark iron plates, brown wrapped grip
- Effect A: a row of rivets down the center of the blade
- Effect B: one small neon magenta dash on the blade
- Effect C: a small cat face stamped on the guard and a hex nut pommel
- Drawings: rivets along the guard and the blade edge, scratches on the iron

### The Godfather

Único sobre a Long Sword. Cabo em cima à direita, ponta embaixo à esquerda. Só o ícone; a wave da Long Sword não muda.

| | |
|---|---|
| Código | `the_godfather` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_the_godfather_icon.png` |
| Wave | `game/assets/weapons/weapon_long_sword.png` |

Categoria:

```text
a long two-hand iron sword a cat would swing with both paws, long broad blade, winged guard, wrapped grip, round pommel, diagonal with the hilt at the upper right and the tip at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: cold iron gray blade, brass wings and collar, dark wrapped grip, purple gem
- Effect A: brass wings around a small cat face on the guard
- Effect B: violet runes painted down the fuller
- Effect C: a round pommel with a purple cat-head gem in a gold ring
- Drawings: brass filigree on the blade base, a wrapped cord on the grip

## Varinhas

Diagonal, cabeça em cima à direita, cabo embaixo à esquerda. A mesma câmera da Long Sword.

### Wand

Ícone aprovado. O sprite que a arma usa dentro da wave continua o pixel antigo.

| | |
|---|---|
| Código | `wand` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_wand_icon.png` |
| Wave | `game/assets/weapons/weapon_wand.png` |

Categoria:

```text
a one-hand wooden wand a cat would point, long slim shaft, crescent head with cat ears, wrapped grip, diagonal with the head at the upper right and the butt at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: dark wood shaft, brass crescent and wire, brown wrapped grip, purple star
- Effect A: a brass crescent with cat ears
- Effect B: a purple star gem set inside the crescent
- Effect C: brass wire spiraling down the shaft
- Drawings: a wrapped grip and a small ring on the wrap

### Spark Needle

Único sobre a Wand. Cabeça em cima à direita, cabo embaixo à esquerda. Só o ícone; a wave da Wand não muda.

| | |
|---|---|
| Código | `spark_needle` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_spark_needle_icon.png` |

Categoria:

```text
a slim one-hand iron wand a cat would point, needle tip, cat-ear head, wrapped grip, pointed pommel, diagonal with the head at the upper right and the butt at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: cold iron gray shaft, brass wire, dark wrapped grip, magenta gem
- Effect A: cat ears flanking a needle tip
- Effect B: one magenta gem set in the head, and a small magenta dash on the shaft
- Effect C: a pointed pommel with a gold ring
- Drawings: brass scroll wire along the shaft, a wrapped cord on the grip

### The Elder Paw

Único de tier 3 sobre a Wand. Cabeça em cima à direita, cabo embaixo à esquerda. Só o ícone; a wave da Wand não muda.

| | |
|---|---|
| Código | `the_elder_paw` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_the_elder_paw_icon.png` |
| Wave | `game/assets/weapons/weapon_wand.png` |

Categoria:

```text
a one-hand master wand a cat would point, dark shaft, cat-head crown holding a purple orb, winged collar, wrapped grip, gem pommel, diagonal with the head at the upper right and the butt at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: dark iron shaft, brass wings and collar, brown wrapped grip, purple gems
- Effect A: a silver cat head with glowing violet eyes, holding a purple orb
- Effect B: violet runes painted down the shaft
- Effect C: a gem pommel with a purple bead, and a small cat face on the collar
- Drawings: brass wings under the head, a wrapped cord on the grip

## Arcos

Diagonal, ponta de cima à direita, ponta de baixo à esquerda. A corda fica do lado esquerdo do arco.

### Short Bow

Ícone aprovado. O sprite que a arma usa dentro da wave continua o pixel antigo, em repouso e armado.

| | |
|---|---|
| Código | `shortbow` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_short_bow_icon.png` |
| Wave | `game/assets/weapons/weapon_shortbow_idle.png` e `weapon_shortbow_drawn.png` |

Categoria:

```text
a short recurve bow a cat would draw, wood limbs, gold feathered tips, two cat heads on the grip, purple wrap, diagonal with the upper limb at the upper right and the lower limb at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: brown wood limbs, brass wings and wire, dark horn tips, purple wrapped grip, magenta dash
- Effect A: gold feathered wings at both limb tips
- Effect B: two gold cat heads flanking the grip
- Effect C: a small magenta dash on the upper limb
- Drawings: brass wire spiraling the limbs, a purple wrap on the grip, a taut string

### Hunter's Recurve

Único sobre o Short Bow. Ponta de cima à direita, ponta de baixo à esquerda. Só o ícone; a wave do Short Bow não muda.

| | |
|---|---|
| Código | `hunters_recurve` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_hunters_recurve_icon.png` |

Categoria:

```text
a short recurve bow a cat would draw, wood limbs, silver cat-head tips, wrapped grip, gold wings, diagonal with the upper limb at the upper right and the lower limb at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: brown wood limbs, silver cat-head tips, dark wrapped grip, gold wings, purple runes
- Effect A: silver cat heads at both limb tips, each with a purple eye
- Effect B: purple runes painted along both limbs and on the silver plates
- Effect C: gold wings at the grip
- Drawings: a wrapped cord on the grip, silver plates with a purple mark, a taut string

## Lanças

Diagonal, ponta em cima à direita, cabo embaixo à esquerda.

### Javelin

Ícone aprovado. O sprite que a arma usa dentro da wave, e o projétil, continuam o pixel antigo.

| | |
|---|---|
| Código | `javelin` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_javelin_icon.png` |
| Wave | `game/assets/weapons/weapon_javelin.png` |

Categoria:

```text
a one-hand iron javelin a cat would throw, spear tip, cat-ear head, wrapped grip, gem pommel, diagonal with the tip at the upper right and the butt at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: dark iron shaft, brass wire, brown wrapped grip, magenta gem, purple pommel bead
- Effect A: a spear head with cat-ear flanges
- Effect B: a magenta diamond gem set in the head, and a small magenta dash on the shaft
- Effect C: a pommel with a purple bead and a small magenta gem
- Drawings: brass scroll wire along the shaft, a wrapped cord on the grip, a gold collar under the head

### Skewer of the Depths

Único sobre a Javelin. Ponta em cima à direita, cabo embaixo à esquerda. Só o ícone; a wave e o projétil da Javelin não mudam.

| | |
|---|---|
| Código | `skewer_of_the_depths` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_skewer_of_the_depths_icon.png` |

Categoria:

```text
a one-hand iron javelin a cat would throw, broad rune blade, braided grip, clawed pommel, diagonal with the tip at the upper right and the butt at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: dark wood shaft, iron blade, brass rings, brown braid, purple runes
- Effect A: a broad spear blade with side barbs
- Effect B: purple runes painted down the blade
- Effect C: a magenta glow at the collar
- Drawings: a braided wrap, three brass rings, a clawed pommel

### The Matriarch

Único de tier 3 sobre a Javelin. Ponta em cima à direita, cabo embaixo à esquerda. Só o ícone; a wave e o projétil da Javelin não mudam.

| | |
|---|---|
| Código | `the_matriarch` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_the_matriarch_icon.png` |
| Wave | `game/assets/weapons/weapon_javelin.png` |

Categoria:

```text
a one-hand ceremonial javelin a cat matriarch would throw, double spear tips, gold cat-head collar, burgundy ribbons, diagonal with the tip at the upper right and the butt at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: dark wood shaft, iron spear tips, gold collar, burgundy ribbons
- Effect A: a gold cat-head collar with fangs under the main tip
- Effect B: two burgundy ribbons hanging from the collar
- Effect C: a smaller spear tip at the butt, with a gold ring
- Drawings: gold filigree on the collar and the butt ring

### Tidefork

Peça do set Whisker Tide, sobre a Javelin. Ponta em cima à direita, cabo embaixo à esquerda. Só o ícone; a wave e o projétil da Javelin não mudam.

| | |
|---|---|
| Código | `tidefork` |
| Mãos | 1 |
| Set | `whisker_tide` |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_tidefork_icon.png` |
| Wave | `game/assets/weapons/weapon_javelin.png` |

Categoria:

```text
a one-hand forked javelin a cat would throw, split iron head, cyan gem, wood shaft, brass wire, pointed pommel, diagonal with the head at the upper right and the butt at the lower left, tall chunky silhouette
```

Personalidade:

- Colors: iron fork, cyan gem, wood shaft, brass wire
- Effect A: a split spear head
- Effect B: a cyan diamond gem set under the fork
- Effect C: a pointed iron pommel
- Drawings: brass wire on the collar and the pommel

## Broquéis

De frente. A forma e as tiras ficam no bloco de cada broquel.

### Buckler

Broquel base. Tampa de garrafa, de frente, com as tiras do lado direito. Só o ícone; a wave continua o pixel do escudo.

| | |
|---|---|
| Código | `buckler` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_buckler_icon.png` |
| Wave | `game/assets/weapons/weapon_small_shield.png` |

Categoria:

```text
a one-hand bottle-cap buckler a cat would raise, crimped metal rim, scratched face with a cat drawing, rust and blue paint, leather straps on the right, facing the camera, chunky silhouette
```

Personalidade:

- Colors: gray metal, rust red, blue paint, brown leather straps
- Effect A: a crimped bottle-cap rim
- Effect B: a scratched cat face on the metal
- Effect C: leather straps tied on the right
- Drawings: scratches, dents, and flecks of rust and blue paint

### Trash Lid Buckler

Único de tier 1 sobre o Buckler. Tampa de lixo, de frente, com a alça do lado direito. Só o ícone; a wave continua o pixel do escudo.

| | |
|---|---|
| Código | `trash_lid_buckler` |
| Mãos | 1 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_trash_lid_buckler_icon.png` |
| Wave | `game/assets/weapons/weapon_small_shield.png` |

Categoria:

```text
a one-hand trash-lid buckler a cat would raise, dented metal lid, rust and blue paint, moss on the handle, leather straps on the right, facing the camera, chunky silhouette
```

Personalidade:

- Colors: gray metal, rust red, blue paint, brown leather, green moss
- Effect A: a dented trash-lid rim
- Effect B: a scratched cat face, with moss on the center handle
- Effect C: leather straps tied on the right
- Drawings: rust, blue paint chips, and a metal loop handle

### Tide Buckler

Peça do set Whisker Tide, sobre o Buckler. Só o ícone; o sprite da wave continua o pixel do Buckler.

| | |
|---|---|
| Código | `tide_buckler` |
| Mãos | 1 |
| Set | `whisker_tide` |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_tide_buckler_icon.png` |
| Wave | `game/assets/weapons/weapon_small_shield.png` |

Categoria:

```text
a one-hand oval buckler a cat would raise, brass rim, dark face, gold filigree, emerald gem, facing the camera, chunky silhouette
```

Personalidade:

- Colors: brass rim, dark iron face, gold filigree, emerald gem
- Effect A: an oval brass rim with rivets
- Effect B: an emerald gem in a gold setting
- Effect C: a grip on the right edge
- Drawings: gold filigree spreading from the gem

## Cajados

Diagonal, cabeça em cima à esquerda, cabo embaixo à direita.

### Staff

Cajado base. Cabeça em cima à esquerda, cabo embaixo à direita. Só o ícone; a wave continua o pixel da varinha. O código no jogo segue `oak_staff`.

| | |
|---|---|
| Código | `oak_staff` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_staff_icon.png` |
| Wave | `game/assets/weapons/weapon_wand.png` |

Categoria:

```text
a two-hand staff a cat would carry, iron lantern head with cat ears, wood shaft, wrapped grip, round metal pommel, diagonal with the head at the upper left and the butt at the lower right, tall chunky silhouette
```

Personalidade:

- Colors: dark iron lantern, brown wood shaft, wrapped grip
- Effect A: cat ears on an iron lantern cage
- Effect B: riveted bands on the shaft
- Effect C: a round metal pommel
- Drawings: vertical bars on the lantern, a wrapped cord on the grip

### Catnip Gnarled Staff

Único de tier 1 sobre o Staff. Cabeça em cima à esquerda, cabo embaixo à direita. Só o ícone; a wave continua o pixel da varinha.

| | |
|---|---|
| Código | `catnip_staff` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_catnip_staff_icon.png` |
| Wave | `game/assets/weapons/weapon_wand.png` |

Categoria:

```text
a two-hand gnarled staff a cat would conjure, twisted wood ring, purple crystal, green leaves, purple flowers, wrapped grip, paw pommel, diagonal with the head at the upper left and the butt at the lower right, tall chunky silhouette
```

Personalidade:

- Colors: dark wood, purple crystal, green leaves, purple flowers, magenta dash, gold coin
- Effect A: a twisted branch ring holding a purple crystal
- Effect B: vines, leaves, and small purple flowers along the shaft
- Effect C: one magenta dash on the shaft, and a paw pommel with a gold coin
- Drawings: a gold clasp, a wrapped grip, a curl of vine

### Moonwhisker Staff

Único de tier 2 sobre o Staff. Só o ícone; a wave do cajado continua o pixel da varinha.

| | |
|---|---|
| Código | `moonwhisker_staff` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_moonwhisker_staff_icon.png` |
| Wave | `game/assets/weapons/weapon_wand.png` |

Categoria:

```text
a two-hand ceremonial staff a cat would conjure, cat-ear gold crown, cyan crystal with a magenta core, dark shaft, cloth tassels, gold spear butt, diagonal with the head at the upper left and the butt at the lower right, tall chunky silhouette
```

Personalidade:

- Colors: dark iron shaft, brass wire, gold crown, cyan crystal, magenta core, pale cloth tassels
- Effect A: a gold cat-ear crown around a cyan crystal with a magenta heart
- Effect B: pale cloth tassels and a small leaf charm under the head
- Effect C: a gold spear butt, and one magenta dash on the shaft
- Drawings: brass scroll wire along the shaft, gold rings, a braided dark grip

### The Grandpurr

Único de tier 3 sobre o Staff. Cabeça em cima à esquerda, ponta embaixo à direita. Só o ícone; a wave e a bola de fogo continuam o pixel antigo.

| | |
|---|---|
| Código | `the_grandpurr` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_the_grandpurr_icon.png` |
| Wave | `game/assets/weapons/weapon_the_grandpurr.png` |

Categoria:

```text
a two-hand spiked staff a cat would conjure, iron cat-skull head, magenta eye, magenta sparks, spiked collar, wrapped grip, spiked pommel with a magenta slot, diagonal with the head at the upper left and the butt at the lower right, tall chunky silhouette
```

Personalidade:

- Colors: dark iron, wrapped brown grip, magenta eye and sparks, orange embers
- Effect A: an iron cat skull with one glowing magenta eye
- Effect B: magenta sparks off the skull, and a magenta slot on the pommel
- Effect C: a spiked pommel with orange embers
- Drawings: a spiked collar, diamond studs, a wrapped grip

## Martelos

Diagonal, cabeça em cima à esquerda, cabo embaixo à direita.

### Hammer

Martelo base. Só o ícone; a wave continua o pixel do martelo.

| | |
|---|---|
| Código | `hammer` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_hammer_icon.png` |
| Wave | `game/assets/weapons/weapon_hammer.png` |

Categoria:

```text
a two-hand iron hammer a cat would swing, block head with cat ears and purple gems, wrapped grip, hex pommel, diagonal with the head at the upper left and the butt at the lower right, chunky silhouette
```

Personalidade:

- Colors: dark iron, purple gems, brown wrapped grip
- Effect A: cat ears on the hammer head
- Effect B: three purple gems set in iron cages
- Effect C: a hex pommel
- Drawings: rivets, a wrapped grip

### Thunder Paw

Único de tier 1 sobre o Hammer. Cabeça em cima à esquerda, cabo embaixo à direita. Só o ícone; a wave do Hammer não muda.

| | |
|---|---|
| Código | `thunder_paw` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_thunder_paw_icon.png` |
| Wave | `game/assets/weapons/weapon_hammer.png` |

Categoria:

```text
a two-hand ceremonial hammer a cat would swing, dark head with a purple eye, gold filigree, cat ears, purple wrapped grip, cat-head pommel, diagonal with the head at the upper left and the butt at the lower right, chunky silhouette
```

Personalidade:

- Colors: dark iron, gold filigree, purple eye, purple wrap
- Effect A: a purple cat eye in the hammer head
- Effect B: cat ears on the head and a cat head on the pommel
- Effect C: gold crisscross wrap on the grip
- Drawings: gold scrollwork across the head

### Immortal King's Claw Crusher

Único de tier 3 sobre o Hammer. Cabeça em cima à esquerda, cabo embaixo à direita. Só o ícone; a wave continua o pixel do martelo.

| | |
|---|---|
| Código | `immortal_claw_crusher` |
| Mãos | 2 |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_immortal_claw_crusher_icon.png` |
| Wave | `game/assets/weapons/weapon_immortal_claw_crusher.png` |

Categoria:

```text
a two-hand claw hammer a cat would swing, thorned head around a purple crystal, iron claws, wrapped grip, clawed pommel with a gold bead, diagonal with the head at the upper left and the butt at the lower right, chunky silhouette
```

Personalidade:

- Colors: dark wood thorns, purple crystal, iron claws, gold bead
- Effect A: a purple crystal caged in thorns
- Effect B: iron claws around the head and on the pommel
- Effect C: a gold bead between the pommel claws
- Drawings: a wrapped grip, loose cloth strips

### The Purrcemaker

Peça do set Purrcemaker, sobre o Hammer. Cabeça em cima à esquerda, cabo embaixo à direita. Só o ícone; a wave continua o pixel do Hammer.

| | |
|---|---|
| Código | `the_purrcemaker` |
| Mãos | 2 |
| Set | `purrcemaker` |
| Ícone (HUD, wiki e catálogo) | `game/assets/weapons/weapon_the_purrcemaker_icon.png` |
| Wave | `game/assets/weapons/weapon_hammer.png` |

Categoria:

```text
a two-hand spiked hammer a cat would swing, iron cat skull with magenta eyes, spiked cheeks, wood haft, spiked pommel, diagonal with the head at the upper left and the butt at the lower right, chunky silhouette
```

Personalidade:

- Colors: dark iron, magenta eyes and slits, brown wood haft
- Effect A: a cat skull with glowing magenta eyes
- Effect B: magenta slits on the spiked cheeks
- Effect C: a spiked pommel
- Drawings: rivets, a stitched wrap on the haft

## Botas

Três quartos, bico embaixo à esquerda e cano em cima à direita.

### Leather Boots

Bota base de couro. Só o ícone; o pixel no gato continua `leather_boots.png`. Stray Striders e Alley Cat Boots ficam no pixel.

| | |
|---|---|
| Código | `leather_boots` |
| Slot | boots |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_leather_boots_icon.png` |
| Pixel | `game/assets/armor/leather_boots.png` |

Categoria:

```text
a leather boot a cat would wear, fur collar and fur toe, rope wraps, fang trim, three-quarter view with the toe at the lower left and the cuff at the upper right, chunky silhouette
```

Personalidade:

- Colors: dark brown leather, tan fur, bone fangs, rope
- Effect A: a fur cuff and a fur paw toe
- Effect B: fangs along the cuff and the toe
- Effect C: rope wrapped around the shaft
- Drawings: straps, stitches, and a small heel

### Iron Boots

Bota base de ferro. Mesma câmera da Leather Boots. Só o ícone; o pixel no gato continua `iron_boots.png`. Iron Fang Greaves e Purrcemaker Sabatons ficam no pixel.

| | |
|---|---|
| Código | `iron_boots` |
| Slot | boots |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_iron_boots_icon.png` |
| Pixel | `game/assets/armor/iron_boots.png` |

Categoria:

```text
an iron boot a cat would wear, battered metal plates over leather, rope wraps, rust, three-quarter view with the toe at the lower left and the cuff at the upper right, chunky silhouette
```

Personalidade:

- Colors: gray iron, rust brown, dark leather, rope
- Effect A: a torn metal cuff
- Effect B: riveted plates over the leather toe
- Effect C: rope wrapped around the shaft
- Drawings: rust, dents, and loose strap ends

## Alley Cat

Quatro peças. Cada uma é um ícone. O pixel de couro das bases fica no lugar.

### Alley Cat Hood

Capuz de frente, orelhas para cima.

| | |
|---|---|
| Código | `alley_cat_hood` |
| Slot | helm |
| Set | `alley_cat` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_alley_cat_hood_icon.png` |
| Pixel | `game/assets/armor/leather_helm.png` |

Categoria:

```text
a leather cat hood a cat would wear, torn ears, stitched brow, brass buckle, scarf, facing the camera, chunky silhouette
```

Personalidade:

- Colors: dark leather, brass buckle, brown patch
- Effect A: torn cat ears
- Effect B: a stitched brow over a dark opening
- Effect C: a brass buckle on the scarf
- Drawings: stitches, a square patch, rivets

### Alley Cat Paws

O par, garras para baixo.

| | |
|---|---|
| Código | `alley_cat_paws` |
| Slot | gloves |
| Set | `alley_cat` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_alley_cat_paws_icon.png` |
| Pixel | `game/assets/armor/leather_gloves.png` |

Categoria:

```text
a pair of leather fingerless gloves a cat would wear, claws, metal plates, brass buckles, wraps, claws pointing down, chunky silhouette
```

Personalidade:

- Colors: dark leather, steel plates, brass buckles
- Effect A: claw tips on the fingers
- Effect B: a metal plate on the back of each paw
- Effect C: brass buckles and cloth wraps
- Drawings: stitches and loose strap ends

### Alley Cat Boots

O par, bicos para baixo à direita.

| | |
|---|---|
| Código | `alley_cat_boots` |
| Slot | boots |
| Set | `alley_cat` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_alley_cat_boots_icon.png` |
| Pixel | `game/assets/armor/leather_boots.png` |

Categoria:

```text
a pair of leather boots a cat would wear, folded cuffs, metal toe plates, claw tips, straps, toes toward the lower right, chunky silhouette
```

Personalidade:

- Colors: dark leather, steel plates, brass buckle
- Effect A: folded cuffs
- Effect B: riveted metal over the toes
- Effect C: a claw on each toe
- Drawings: stitches, a brass buckle, and a loose strap

### Alley Cat Bell

Coleira de frente, o sino pendurado.

| | |
|---|---|
| Código | `alley_cat_bell` |
| Slot | collar |
| Set | `alley_cat` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_alley_cat_bell_icon.png` |
| Pixel | `game/assets/armor/leather_collar.png` |

Categoria:

```text
a leather collar a cat would wear, brass bell, feathers, a key charm, studs, facing the camera, chunky silhouette
```

Personalidade:

- Colors: dark leather, brass bell and buckle, gray feathers
- Effect A: a brass bell
- Effect B: feathers on the left
- Effect C: a key charm on the right
- Drawings: studs, a buckle, and frayed cloth

## Iron Fang

Quatro peças. Cada uma é um ícone. O pixel de ferro das bases fica no lugar.

### Iron Fang Helm

Elmo de lobo, de três quartos, virado para a esquerda.

| | |
|---|---|
| Código | `iron_fang_helm` |
| Slot | helm |
| Set | `iron_fang` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_iron_fang_helm_icon.png` |
| Pixel | `game/assets/armor/iron_helm.png` |

Categoria:

```text
an iron wolf helm a cat would wear, plated snout, fangs, gold trim, torn mane, three-quarter view facing left, chunky silhouette
```

Personalidade:

- Colors: dark iron, gold trim, bone fangs
- Effect A: a wolf snout with an open jaw
- Effect B: gold diamond on the brow
- Effect C: a torn mane with gold edges
- Drawings: rivets and ear plates

### Iron Fang Plate

Peitoral de frente, oco no pescoço.

| | |
|---|---|
| Código | `iron_fang_plate` |
| Slot | chest |
| Set | `iron_fang` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_iron_fang_plate_icon.png` |
| Pixel | `game/assets/armor/iron_chest.png` |

Categoria:

```text
an iron chest plate a cat would wear, spiked shoulders, fang collar, gold trim, chainmail, facing the camera, chunky silhouette
```

Personalidade:

- Colors: dark iron, gold trim, bone spikes
- Effect A: a fang-lined collar
- Effect B: spiked pauldrons
- Effect C: gold chevrons on the belly
- Drawings: buckles and chainmail

### Iron Fang Gauntlets

O par, garras para baixo.

| | |
|---|---|
| Código | `iron_fang_gauntlets` |
| Slot | gloves |
| Set | `iron_fang` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_iron_fang_gauntlets_icon.png` |
| Pixel | `game/assets/armor/iron_gloves.png` |

Categoria:

```text
a pair of iron gauntlets a cat would wear, clawed fingers, spikes, gold trim, claws pointing down, chunky silhouette
```

Personalidade:

- Colors: dark iron, gold trim, bone claws
- Effect A: clawed fingers
- Effect B: spikes on the wrist and the back of the hand
- Effect C: gold edging on the plates
- Drawings: leather straps and chainmail

### Iron Fang Greaves

O par, garras para baixo.

| | |
|---|---|
| Código | `iron_fang_greaves` |
| Slot | boots |
| Set | `iron_fang` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_iron_fang_greaves_icon.png` |
| Pixel | `game/assets/armor/iron_boots.png` |

Categoria:

```text
a pair of iron greaves a cat would wear, clawed toes, knee spikes, gold trim, claws pointing down, chunky silhouette
```

Personalidade:

- Colors: dark iron, gold trim, bone claws
- Effect A: clawed toes
- Effect B: a spike on each knee
- Effect C: gold edging on the plates
- Drawings: buckles and chainmail

## Purrcemaker

A armadura do set. O martelo já tem ícone. O texto da folha não entra. O pixel de ferro fica no lugar.

### Purrcemaker Crown

De três quartos, virado para a direita.

| | |
|---|---|
| Código | `purrcemaker_crown` |
| Slot | helm |
| Set | `purrcemaker` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_purrcemaker_crown_icon.png` |
| Pixel | `game/assets/armor/iron_helm.png` |

Categoria:

```text
a spiked iron crown a cat would wear, cat-skull face, magenta eyes, magenta slits, three-quarter view facing right, chunky silhouette
```

Personalidade:

- Colors: dark iron, magenta eyes and slits, rust
- Effect A: a cat skull with magenta eyes
- Effect B: magenta slits on the cheek plates
- Effect C: spikes and cat ears
- Drawings: a buckle and rust

### Purrcemaker Plate

De frente, oco no pescoço.

| | |
|---|---|
| Código | `purrcemaker_plate` |
| Slot | chest |
| Set | `purrcemaker` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_purrcemaker_plate_icon.png` |
| Pixel | `game/assets/armor/iron_chest.png` |

Categoria:

```text
a spiked iron chest plate a cat would wear, cat-skull boss, magenta slits, spiked pauldrons, facing the camera, chunky silhouette
```

Personalidade:

- Colors: dark iron, magenta slits, rust
- Effect A: a cat skull on the chest
- Effect B: magenta slits beside the skull and on the belly
- Effect C: spiked pauldrons
- Drawings: buckles, chainmail, and rust

### Purrcemaker Gauntlets

O par, garras para baixo à direita.

| | |
|---|---|
| Código | `purrcemaker_gauntlets` |
| Slot | gloves |
| Set | `purrcemaker` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_purrcemaker_gauntlets_icon.png` |
| Pixel | `game/assets/armor/iron_gloves.png` |

Categoria:

```text
a pair of spiked iron gauntlets a cat would wear, clawed fingers, magenta slits, skull plates, claws toward the lower right, chunky silhouette
```

Personalidade:

- Colors: dark iron, magenta slits, rust
- Effect A: clawed fingers
- Effect B: magenta slits on the skull plates
- Effect C: spikes along the forearm
- Drawings: buckles and rust

### Purrcemaker Sabatons

O par, garras para baixo.

| | |
|---|---|
| Código | `purrcemaker_sabatons` |
| Slot | boots |
| Set | `purrcemaker` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_purrcemaker_sabatons_icon.png` |
| Pixel | `game/assets/armor/iron_boots.png` |

Categoria:

```text
a pair of spiked iron sabatons a cat would wear, clawed toes, magenta slits, claws pointing down, chunky silhouette
```

Personalidade:

- Colors: dark iron, magenta slits, rust
- Effect A: clawed toes
- Effect B: a magenta slit on each shin
- Effect C: spikes on the cuff and the toe
- Drawings: buckles, chainmail, and rust

## Street Scrapper

Quatro peças. Cada uma é um ícone. O pixel de couro das bases fica no lugar.

### Scrapper's Cap

Capacete de aviador, de três quartos, virado para a esquerda.

| | |
|---|---|
| Código | `scrappers_cap` |
| Slot | helm |
| Set | `street_scrapper` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_scrappers_cap_icon.png` |
| Pixel | `game/assets/armor/leather_helm.png` |

Categoria:

```text
a leather aviator cap a cat would wear, cat ears, cracked goggles, bandana, three-quarter view facing left, chunky silhouette
```

Personalidade:

- Colors: brown leather, dark bandana, steel goggles
- Effect A: cat ears
- Effect B: cracked goggles
- Effect C: a tied bandana
- Drawings: stitches and a brim

### Box Fort Vest

Colete de frente, oco no pescoço, pneu no ombro esquerdo.

| | |
|---|---|
| Código | `box_fort_vest` |
| Slot | chest |
| Set | `street_scrapper` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_box_fort_vest_icon.png` |
| Pixel | `game/assets/armor/leather_chest.png` |

Categoria:

```text
a scrap vest a cat would wear, tire pauldron, metal plates, pockets, nails, facing the camera, chunky silhouette
```

Personalidade:

- Colors: brown leather, blue cloth, rusted steel, black tire
- Effect A: a tire on the left shoulder
- Effect B: nailed metal on the right shoulder
- Effect C: pockets and a chest plate
- Drawings: straps, rope, and torn cloth

### Padded Alley Paws

O par, garras para baixo.

| | |
|---|---|
| Código | `padded_alley_paws` |
| Slot | gloves |
| Set | `street_scrapper` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_padded_alley_paws_icon.png` |
| Pixel | `game/assets/armor/leather_gloves.png` |

Categoria:

```text
a pair of leather gloves a cat would wear, claw tips, knuckle plates, wraps, claws pointing down, chunky silhouette
```

Personalidade:

- Colors: brown leather, steel plates, rope
- Effect A: claw tips
- Effect B: a metal plate on each paw
- Effect C: buckles and wraps
- Drawings: studs and stitches

### Stray Striders

O par, bicos para baixo à esquerda.

| | |
|---|---|
| Código | `stray_striders` |
| Slot | boots |
| Set | `street_scrapper` |
| Ícone (HUD, wiki e catálogo) | `game/assets/armor/armor_stray_striders_icon.png` |
| Pixel | `game/assets/armor/leather_boots.png` |

Categoria:

```text
a pair of worn leather boots a cat would wear, metal toe caps, laces, patches, toes toward the lower left, chunky silhouette
```

Personalidade:

- Colors: brown leather, steel toes, olive patches
- Effect A: metal toe caps
- Effect B: crossed laces
- Effect C: sewn patches
- Drawings: a buckle, stitches, and scuffs

## Peitorais únicos

De frente. Recortados da folha e ampliados 3×. O pixel no gato continua o da base.

### Leather Armor

Chest 1, redesenho em 1024. Ícone `game/assets/armor/armor_leather_chest_icon.png`. Pixel `leather_chest.png`.

### Brasswhisker Harness

Chest 2. Único de couro, tier 1. Código `brasswhisker_harness`. Ícone `armor_brasswhisker_harness_icon.png`.

### Witchwhisker Vest

Chest 3. Único de couro, tier 2. Código `witchwhisker_vest`. Ícone `armor_witchwhisker_vest_icon.png`. O roxo da aura ficou na borda.

### Iron Armor

Chest 4, redesenho em 1024. Ícone `game/assets/armor/armor_iron_chest_icon.png`. Pixel `iron_chest.png`.

### Blackpaw Cuirass

Chest 5. Único de ferro, tier 2. Código `blackpaw_cuirass`. Ícone `armor_blackpaw_cuirass_icon.png`.

### Hellwhisker Plate

Chest 6. Único de ferro, tier 3. Código `hellwhisker_plate`. Ícone `armor_hellwhisker_plate_icon.png`.

## Colares

De frente, o buraco do pescoço vazado. Recortados da folha e ampliados até 1024. O pixel no gato continua o da base. O Collar 3 ficou de fora.

### Leather Collar

Collar 1. Ícone `game/assets/armor/armor_leather_collar_icon.png`. Pixel `leather_collar.png`.

### Lucky Jingle Bell

Collar 2. Ícone `armor_lucky_jingle_bell_icon.png`. Pixel `leather_collar.png`.

### Iron Collar

Collar 4. Ícone `game/assets/armor/armor_iron_collar_icon.png`. Pixel `iron_collar.png`.

### Goldfang Gorget

Collar 5. Único de ferro, tier 1. Código `goldfang_gorget`. Ícone `armor_goldfang_gorget_icon.png`.

### Violetchain Gorget

Collar 6. Único de ferro, tier 2. Código `violetchain_gorget`. Ícone `armor_violetchain_gorget_icon.png`. O magenta fica no metal.

## Luvas base

Garras para baixo. Recortadas da folha e ampliadas até 1024. O pixel no gato continua o da base.

### Leather Gloves

Luva 2. Ícone `game/assets/armor/armor_leather_gloves_icon.png`. Pixel `leather_gloves.png`.

### Iron Gloves

Luva 5. Ícone `game/assets/armor/armor_iron_gloves_icon.png`. Pixel `iron_gloves.png`.

## Elmos

De frente. Recortados da folha e ampliados até 1024. O pixel no gato continua o da base. Os elmos 1 e 3 ficaram de fora.

### Leather Helm

Elmo 2. Ícone `game/assets/armor/armor_leather_helm_icon.png`. Pixel `leather_helm.png`.

### Swiftwhisker Cowl

Elmo 4. Único de couro, tier 3, destreza. Código `swiftwhisker_cowl`. Ícone `armor_swiftwhisker_cowl_icon.png`. Sobe velocidade de ataque, crítico e movimento.

### Iron Helm

Elmo 5. Ícone `game/assets/armor/armor_iron_helm_icon.png`. Pixel `iron_helm.png`.

### Sigon's Polished Visor

Elmo 6. Ícone `armor_sigon_visor_icon.png`. O sprite do set continua `armor_sigon_visor.png`.

### Sigon's Wrought Iron Plate

Peitoral da folha. Ícone `armor_sigon_chest_icon.png`. O sprite continua `armor_sigon_chest.png`.

### Sigon's Articulated Gauntlets

Luva da folha. Ícone `armor_sigon_gauntlets_icon.png`. O sprite continua `armor_sigon_gauntlets.png`.

### Sigon's Gleaming Sabatons

Par de botas da folha. Ícone `armor_sigon_sabaton_icon.png`. O sprite continua `armor_sigon_sabaton.png`.

### Goldmaw Helm

Elmo 7. Único de ferro, tier 2. Código `goldmaw_helm`. Ícone `armor_goldmaw_helm_icon.png`.

### Helm of Domi-meow-tion

Elmo 8. Ícone `armor_helm_of_domi_meow_tion_icon.png`. O sprite continua `armor_helm_of_domi_meow_tion.png`.

## Próximo item

### {Nome}

| | |
|---|---|
| Código | |
| Mãos / slot | |
| Arquivo | |

Categoria:

```text

```

Personalidade:

- Colors:
- Effect A:
- Effect B:
- Effect C:
- Drawings:
