# 05 — Monster — Gutter Cloud

Shooter do beco. O nome e o beco ficam neste arquivo. No jogo o código continua `shooter`.

A nuvem já está cortada. A fileira pronta é `cloud/sheet.png`: dezesseis células de 96×96. O registro do corte está em [cloud/README.md](../cloud/README.md).

Ela flutua. O código faz o balanço. A sheet é o crepitar: olhos acesos e faíscas curtas na massa. O tiro é o raio em [cloud/bolt/README.md](../cloud/bolt/README.md): o início toca uma vez, a viagem fica em loop, e o código leva o projétil.

## Corpo

Nuvem baixa e larga, vapor azul-acinzentado, olhos de ciano e magenta pintados na massa, faíscas curtas. Sem perna, sem asa, sem braço. O casco de baixo é uma curva lisa. Cabe na célula, larga, com a base perto do chão da célula.

Recusa se aparecer perna, braço, chão, sombra ou pedestal, ou se a faísca for o único raio do tiro. Ciano e magenta no corpo são figurino. Verde no corpo vaza no corte.

## O que colar no jogo

Cola o bloco abaixo no agente do Purrfect Storm.

```text
Troca o Slingshot Kid pela Gutter Cloud. O código continua shooter. O desenho novo substitui o menino. HP, dano, velocidade, chase_and_shoot, projectile_speed, fire_rate, pesos de onda e os outros monstros continuam os que já estão. O projétil continua o de game/enemies/enemy_projectile.tscn e enemy_projectile.gd. As faíscas desta sheet são o crepitar do corpo. A poça e o raio que cai vêm num arquivo separado, depois.

Usa este PNG exatamente, sem recortar, sem reescalar e sem tirar o fundo de novo:

C:\Users\Grabert\Repos\ai-game-spritesheets\cloud\sheet.png

Ele entra no lugar de game/assets/enemies/enemy_shooter.png. São 1536×96, dezesseis células de 96×96, RGBA. O casco da nuvem encosta na base da célula. A prévia do tempo está em C:\Users\Grabert\Repos\ai-game-spritesheets\cloud\preview\crackle.gif.

Em game/config/enemy_visuals.json, no bloco shooter: display_name passa a Gutter Cloud. locomotion continua floater. jelly_mass continua 0.4. texture_filter passa a linear. sheet_frames = 16. faces_right = false. foot_anchor continua [0.5, 0.98]. Um clipe só, chamado walk, em loop, frames 0 a 15 nessa ordem, seconds_per_frame 0.08. O shooter não dá dash, então esse bloco não ganha charge nem fly.

Em shooter_visual.tres, display_name passa a Gutter Cloud e a textura aponta para o PNG novo. sheet_frames = 16. O filtro fica linear. locomotion continua floater (2).

O clipe dura cerca de 1,3 s. Se o crepitar parecer lento perto da velocidade 128, encurta na direção de 0,9 s. O balanço continua no floater, amplitude 5. A nuvem não pula. O sprite não anda dentro da célula.

Testa no mapa 1: a onda do shooter mostra a nuvem baixa e larga, olhos acesos, faísca piscando, flutuando, virando quando muda de lado. O Slingshot Kid não aparece mais. O tiro que sai ainda é o projétil antigo.
```

## O raio

Quatro frames. As células 0, 1 e 2 são o raio saindo, uma vez. As células 2 e 3 são só a viagem, em loop. A célula 2 é a mesma pose nos dois. Cola o bloco abaixo no agente do Purrfect Storm. O corpo da nuvem já colocado fica quieto.

```text
Troca o desenho do projétil do shooter pelo raio da Gutter Cloud. A cena continua game/enemies/enemy_projectile.tscn, e enemy.gd continua apontando para res://enemies/enemy_projectile.tscn. Dano, velocidade, tempo de vida, fire_rate, projectile_speed, o corpo da nuvem, enemy_visuals.json e os outros monstros continuam os que já estão.

Copia este PNG para game/assets/enemies/projectile_bolt.png, sem recortar e sem reescalar:

C:\Users\Grabert\Repos\ai-game-spritesheets\cloud\bolt\sheet.png

São 384×48, quatro células de 96×48, RGBA. A cauda está à esquerda e a ponta à direita. O saindo está em C:\Users\Grabert\Repos\ai-game-spritesheets\cloud\bolt\preview\saindo.gif. A viagem está em C:\Users\Grabert\Repos\ai-game-spritesheets\cloud\bolt\preview\viajando.gif.

No sprite do projétil, tira o recorte do spritesheet.png e o modulate roxo. A textura passa a ser projectile_bolt.png. hframes = 4, vframes = 1, region desligado, filtro linear, scale 1, centered ligado, offset (-48, 0). A ponta fica na origem do nó. O círculo de colisão continua na origem, raio 14. rotation continua direction.angle().

No script do projétil, o movimento fica o que já está. Acrescenta só o frame. Células 0, 1 e 2 tocam uma vez, nesta ordem, 0,09 s, 0,09 s e 0,14 s: a faísca, o raio crescendo, a ponta no fim. A partir daí, células 2 e 3 entram em loop, 0,07 s cada. O comprimento fica parado. Só o zigue-zague troca. O projétil some no mesmo caso de hoje, no jogador, na parede ou no fim do tempo.

Testa no mapa 1: o shooter solta o raio para a direita do desenho, na direção do gato. Ele sai curto e chega no tamanho final, e daí só pisca enquanto viaja. O miolo roxo antigo não aparece mais.
```
