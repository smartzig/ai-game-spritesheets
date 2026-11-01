# Nuvem da sarjeta — o que ficou

Shooter do mapa 1. O nome no jogo é Gutter Cloud, no lugar do Slingshot Kid. O código continua `shooter`. O corpo crepita. O raio é outro desenho, em [bolt/README.md](bolt/README.md): dois frames de início e dois de viagem.

O corpo é uma fileira de dezesseis poses. A nuvem fica parada na célula. O jogo é que flutua e que anda. Os raios finos no corpo são o crepitar da nuvem, não o tiro.

O still e o papel no beco estão em [05-monster gutter-cloud.md](../prompts-2.5d/05-monster%20gutter-cloud.md). O corte do verde está em `.cursor/skills/cut-chroma-frames/`.

## Identidade

Nuvem baixa e larga, vapor azul-acinzentado, olhos de ciano e magenta pintados na massa, faíscas curtas no corpo. Sem perna, sem asa, sem braço. Luz só de cima à esquerda. Fundo transparente, sem chão, sem sombra, sem pedestal.

## De onde veio

O Sprite Smithy exportou 34 frames de 512×512, já com transparência e ainda com franja verde. Vários frames eram o mesmo desenho repetido. O corte tirou a franja e manteve o ciano e o magenta. Os 34 ficaram em `cut/`. O teste do script deu `ok` em todos: excesso de verde no opaco em 0.

## A fileira

`sheet.png` é o arquivo do jogo. Dezesseis células de 96×96, no total 1536×96. O mesmo enquadramento em todas: a massa cabe na célula, o casco encosta na base (pixel 93), e a faísca não é cortada. A prévia do tempo está em `preview/crackle.gif`, cerca de 1,3 s.

Ordem, da esquerda para a direita, a partir de `cut/`:

`frame-0001`, `frame-0004`, `frame-0007`, `frame-0009`, `frame-0010`, `frame-0013`, `frame-0015`, `frame-0016`, `frame-0019`, `frame-0021`, `frame-0022`, `frame-0025`, `frame-0028`, `frame-0030`, `frame-0033`, `frame-0034`.

O ciclo abre e fecha na nuvem quieta. No meio, as faíscas acendem e apagam. O corpo quase não sobe: o balanço fica no código, no floater.

Conferir `qa/sheet-white.png` (halo verde) e `qa/sheet-black.png` (buraco no olho ou na faísca). Esta fileira passou.

## O que o jogo recebe

O PNG entra no lugar de `game/assets/enemies/enemy_shooter.png`. O clipe se chama `walk`, em loop, frames 0 a 15, 0,08 s cada. Locomoção `floater`, `jelly_mass` 0,4, filtro linear, `faces_right` false, `foot_anchor` (0,5, 0,98). HP, dano, velocidade e cadência ficam como estão. O raio está em `bolt/sheet.png`.
