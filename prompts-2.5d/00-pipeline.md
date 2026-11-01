# Pipeline ativo — do personagem até o vídeo

Preencha os campos uma vez e reutilize os mesmos valores em todo prompt. O que não muda é o visual do jogo.

## O que fica igual em todo personagem

- Ilustração pintada, com volume. Sem pixel art e sem pelo ou pele fotorreal.
- Uma luz só, vinda do alto à esquerda.
- Fundo chroma `#00FF00` no anchor e na T-pose para o Meshy.
- No vídeo, perfil lateral estrito para a esquerda, chroma `#00FF00`, personagem no vazio, sem chão e sem sombra. A caminhada é um loop. O parado é um segundo clipe, no mesmo enquadramento.
- Biblioteca gótica só no box art e na T-pose com cenário. O resto é fundo chapado.

## O que você troca por personagem

| Campo | O que escrever |
|---|---|
| `{CHARACTER_NAME}` | Nome |
| `{CHARACTER_ARCHETYPE}` | Arquétipo, em poucas palavras |
| `{CORE_IDENTITY}` | Espécie, rosto, cores do corpo |
| `{COSTUME_AND_COLOR_PALETTE}` | Roupa e paleta |
| `{CHARACTER_SPECIFIC_BIOME}` | Cenário do box art, no mesmo mundo da biblioteca gótica |
| `{EMPTY_LIMB}` | Pata ou mão que fica vazia, sem efeito mágico |

## Onde está cada prompt

| Passo | Arquivo | O que colar |
|---|---|---|
| 01 Box art | [01-box-art.md](01-box-art.md) | Texto no Google Flow, sem imagem |
| 02 South anchor | [02-south-anchor.md](02-south-anchor.md) | Texto + box art aprovado |
| 03 Neutral | [03-neutral-anchor.md](03-neutral-anchor.md) | Texto + south anchor |
| 03b T-pose | [03b-tpose.md](03b-tpose.md) | Dois textos: cenário, depois chroma |
| Meshy | [03b-tpose.md](03b-tpose.md) | Sem prompt. Sobe o PNG transparente da T-pose |
| 04 Vídeo oeste | [04-walk-video.md](04-walk-video.md) | Um vídeo de caminhada para a esquerda |
| Corte sem halo | `.cursor/skills/cut-chroma-frames/` | PNG transparente a partir do chroma `#00FF00` |
| 06 Itens | [06-items.md](06-items.md) | Chapa única. Cada item guarda a frase de categoria |
| 07 Mapas | [07-maps.md](07-maps.md) | Um PNG 2560×1440. A parede fica na faixa da borda |

Exemplo já preenchido da Pinduca: os arquivos `* pinduca.md` ao lado de cada passo. O vídeo dela está em [04-walk-video pinduca.md](04-walk-video%20pinduca.md). O box art do Zigo está em [01-box-art zigo.md](01-box-art%20zigo.md). O select e o portrait da Michi estão em [01-box-art michi.md](01-box-art%20michi.md): `michi/select.jpg` (688×1024) e `michi/portrait.jpg` (256×256). O esboço do south anchor, ainda sem imagem, está em [02-south-anchor michi.md](02-south-anchor%20michi.md).

## Meshy

Não há um prompt de texto para o modelo 3D. O Meshy usa a imagem.

1. Aprove a T-pose no chroma `#00FF00`.
2. Remova o verde e suba o PNG transparente.
3. Baixe o modelo e os prints das vistas.
4. Esses prints viram o personagem salvo no Google Flow. O vídeo do passo 04 usa esse personagem.

## Depois do vídeo

Não há prompt. Exporte os frames, monte a sheet no Sprite Smithy e espelhe o oeste para obter o leste. Parado e caminhada são trechos da mesma sheet.

## Monstros

O herói acima é perfil lateral. O monstro é três quartos, numa fileira de seis poses, um ciclo de cerca de dois segundos. O prompt está em [05-monster.md](05-monster.md). Você troca `{MONSTER}` e `{MOTION}`.

O pombo é o primeiro que ficou pronto. O still e o voo para colar estão em [05-monster pigeon.md](05-monster%20pigeon.md). O ciclo que vale é o voo: o corpo sobe e desce com as asas abertas. A sheet de chão, só com cabeça e pé, não leu no tamanho do jogo. O registro está em [pigeon/README.md](../pigeon/README.md).

O Alley Rat King é o tanque lento. O still e o dash para colar estão em [05-monster alley-rat-king.md](05-monster%20alley-rat-king.md). Ele ocupa mais quadro que o pombo. O dash é a investida da barriga, e o movimento também está em [05-monster.md](05-monster.md), na seção Charge.

A Gutter Cloud é o shooter. A fileira do corpo está em [cloud/README.md](../cloud/README.md). O raio, com o início e a viagem, está em [cloud/bolt/README.md](../cloud/bolt/README.md). Os blocos para colar no jogo estão em [05-monster gutter-cloud.md](05-monster%20gutter-cloud.md).
