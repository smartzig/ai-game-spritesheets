# Raio — o que ficou

Projétil da Gutter Cloud. São dois ciclos e quatro frames. O início toca uma vez. A viagem fica em loop enquanto o código leva o raio.

O Sprite Smithy exportou 38 frames de 512. Metade era o mesmo desenho repetido, e o meio era o raio crescendo aos poucos. O jogo move o projétil, então esse crescimento não entra. O corte tirou a franja verde e manteve o ciano. Os 38 ficaram em `cut/`. O teste deu `ok` em todos.

## Os dois ciclos

`sheet.png` é uma fileira só. Quatro células de 96×48, no total 384×48. A cauda fica à esquerda. A ponta aponta para a direita. O losango saiu: ele não é o raio saindo.

| Células | Clipe | Frames de origem | O que acontece |
|---|---|---|---|
| 0–2 | saindo, uma vez | `frame-0001`, `frame-0016`, `frame-0037` | A faísca vira o raio e a ponta chega no fim da célula. 0,09 s, 0,09 s e 0,14 s. |
| 2–3 | viajando, em loop | `frame-0037`, `frame-0034` | O raio já no tamanho final. Só o zigue-zague troca. A ponta não anda. 0,07 s cada. |

A célula 2 fecha o saindo e abre a viagem. Duas prévias: `preview/saindo.gif` e `preview/viajando.gif`.

Conferir `qa/sheet-white.png` e `qa/sheet-black.png`. Esta fileira passou.

## O que o jogo recebe

O PNG entra em `game/assets/enemies/projectile_bolt.png`. A cena continua `game/enemies/enemy_projectile.tscn`. O desenho antigo, o recorte do `spritesheet.png` e o tom roxo saem. O raio aponta para a direita, o filtro é linear, e a ponta fica na origem do nó para o acerto continuar na frente. Dano, velocidade, alcance e o corpo da nuvem ficam como estão.
