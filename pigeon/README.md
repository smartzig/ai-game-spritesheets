# Pombo — o que ficou

Monstro leve do beco. O ciclo que entrou é uma fileira de seis poses, três quartos, no chroma verde. O corpo sobe e desce com as asas abertas. Cabeça e pé sozinhos não leram no tamanho do jogo.

O still e o voo para colar estão em [05-monster pigeon.md](../prompts-2.5d/05-monster%20pigeon.md). O corte do verde está em `.cursor/skills/cut-chroma-frames/`.

## Identidade

Pombo de rua gordo, peito estufado, penas cinza bagunçadas, pescoço iridescente, pernas curtas, cara irritada, silhueta compacta e larga. Marcas pequenas de magenta e ciano no corpo. Luz só de cima à esquerda. Fundo `#00FF00` chapado, sem chão, sem sombra, sem pedestal.

## As duas sheets

| Sheet | Arquivo | Tamanho | O que acontece |
|---|---|---|---|
| Chão | `source/sheet.png` | 1024×571 | Seis células. Pés e cabeça mexem pouco. Tem uma plaquinha de papelão nas costas. Movimento pequeno demais. |
| Voo | `fly/source/sheet-good.png` | 1024×254 | A que vale. Sem plaquinha. Asas abertas. O corpo viaja muito para cima e para baixo. O peito não vira de perfil e o pombo não anda para o lado. |

Poses do voo, da esquerda para a direita: corpo baixo, corpo alto, ainda alto começando a descer, corpo baixo de novo, corpo alto, descendo de volta ao baixo. Um ciclo, cerca de dois segundos, no máximo dezesseis frames. Seis poses é o alvo.

As duas imagens de origem têm seis pássaros. As pastas `frames/` e `fly/frames/` hoje têm só `00`–`04`. A sexta célula de cada sheet ainda não está cortada.

## Corte

O verde da sheet de voo não é `#00FF00` puro. A borda mede cerca de `(0.08, 0.94, 0.04)`. `fly/source/cut_good.py` mede essa cor, tira o verde que toca a borda e desmistura a franja. Ciano e magenta no pescoço ficam.

Conferir `fly/qa/good-white.png` (halo verde) e `fly/qa/good-black.png` (buraco na pena ou na marca). Frame com halo ou buraco não segue.

## O que copiar no próximo monstro

- Uma frase de corpo, cor, um detalhe pequeno e a silhueta.
- Uma frase de movimento com a pose 1 até a pose 6, parado na célula.
- Uma mudança óbvia. No pombo foi a altura mais as asas.
- Fileira horizontal de seis células iguais, câmera travada, três quartos.
- Cortar o chroma e olhar o QA no branco e no preto antes de usar.
