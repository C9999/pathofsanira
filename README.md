# Path of Sanira — Escopo e fases

## 1. Visão geral

Endless run para o navegador do celular, no estilo de Alto's Adventure: cenário fluido, ritmo calmo, controle por toques na tela.

No início de cada corrida é feita uma tiragem de tarot: 3 cartas são sorteadas e cada uma dá um poder à personagem, no estilo dos upgrades de Mega Man X. No fim da corrida, o jogo mostra uma frase baseada nas cartas sorteadas e na pontuação.

## Decisões já tomadas

- **Tecnologia:** HTML5 (canvas + JavaScript), rodando direto no navegador do celular, sem instalação.
- **Estilo visual:** simples, com formas planas e cores suaves.
- **Nome:** Path of Sanira.
- **Orientação:** paisagem.
- **Controle:** toques em qualquer ponto da tela, sem botões fixos.
- **Cartas:** as 12 cartas da tela "Cartas e poderes" (grid 3x4) são o modelo atual, com a arte e os poderes descritos na seção 6.
- **Personagem:** a Sanira levita em posição de ioga (lótus), vista de frente, com uma aura ao redor. Detalhes na seção 7.
- **Cenário:** descida de uma ladeira de montanha, céu limpo, obstáculos no caminho e uma moeda no fim. Referência na seção 8.
- **Descartado:** a ideia anterior (menina de bicicleta fugindo de um jacaré, com pedras e galhos) e o dino do jogo original.

## 2. Regras principais

- **Plataforma:** navegador de celular, em paisagem, sem instalação. Hospedagem estática (GitHub Pages).
- **Controles:** só toques, e a tela inteira é a área de toque. Proposta inicial:
  - toque = pular;
  - segurar no ar = habilidade de pairar (se a carta der esse poder);
  - toque duplo ou deslize = habilidade ativa (se houver).
- **Tiragem:** 3 cartas dos 22 Arcanos Maiores, sem repetição.
  - A **1ª carta é a Força em 90% das vezes**.
  - Nos outros 10%, a 1ª carta é uma das outras 21, com a mesma chance.
  - As cartas 2 e 3 são sorteadas com chance igual entre as restantes.
- **Poderes:** cada carta tem um poder (passivo ou ativo) que vale durante a corrida inteira.
- **Pontuação:** contador de pontos no canto superior direito da tela.
- **Reações da personagem:** ao bater em um obstáculo, cair em um buraco ou ser atingida por um inimigo, o rosto dela fica triste por 0,5 segundo e depois volta ao sorriso.
- **Fim da corrida:** pontuação + frase gerada a partir das cartas e da pontuação.

```text
sortear():
  deck = 22 arcanos maiores
  c1 = Força com 90%; senão, uma das outras 21 (uniforme)
  restantes = deck - {c1}
  c2, c3 = duas cartas distintas de restantes (uniforme)
```

## 3. Fora do escopo inicial

- Cartas invertidas, Arcanos Menores e mais de 3 cartas por corrida.
- Ranking online e contas de usuário.
- Compras, anúncios e multijogador.

## 4. Fases

### Fase 0 — Preparação

- Preparar a página para paisagem: aviso para girar o aparelho quando estiver em retrato, tela cheia opcional e bloqueio de zoom e rolagem por toque.
- Decidir se o código parte do t-rex-runner atual ou de um loop novo em canvas. Para o estilo Alto, um loop novo tende a ser mais simples. Se reaproveitar código, manter os créditos e a licença (ver README).
- Definir pasta, padrões de código e como testar no celular (rede local ou GitHub Pages).

**Pronto quando:** repositório organizado e uma página vazia abre no celular.

### Fase 1 — Protótipo do endless run

- Loop do jogo em canvas, com tela cheia e suporte a telas de alta densidade.
- Terreno contínuo de ladeira de montanha, com inclinações suaves e câmera acompanhando a personagem.
- A personagem desce a ladeira levitando, sem correr; toque faz pular.
- Pontuação por distância, tela de fim de corrida e botão de recomeçar.

**Pronto quando:** dá para descer, pular e perder, a 60 fps num celular comum.

### Fase 2 — Mundo e obstáculos

- Geração procedural de obstáculos e dificuldade crescente.
- Colisão, camadas de fundo com efeito de profundidade, ciclo de dia e noite.
- Arte da personagem (seção 7), do cenário e dos obstáculos (seção 8) integrada ao jogo, no estilo simples, com formas planas e cores suaves.
- Reação de rosto triste por 0,5 s nos três casos de dano, com a troca de rosto feita pelas camadas do SVG.

**Pronto quando:** uma corrida de 2 a 3 minutos é jogável e variada, sem cartas ainda.

### Fase 3 — Sistema de cartas

- Dados das cartas em um arquivo JSON (nome, número, texto, poder, ícone), começando pelas 12 cartas da seção 6.
- Sorteio com a regra de 90% para a Força, com testes automáticos da distribuição.
- Tela de tiragem animada: 3 cartas viradas uma a uma, depois a corrida começa.
- Estrutura de poderes modular: cada poder é um módulo que altera parâmetros do jogo (pulo, velocidade, vidas, etc.).
- Mostrar as cartas ativas no HUD.
- Aplicar a cor do poder sorteado (seção 9) nas faixas das mangas e no V do peito da personagem (seção 7).
- Ligar a aura laranja só quando a Força estiver ativa; sem ela, aura fina cinza clara.

**Pronto quando:** toda corrida começa com uma tiragem e o HUD mostra as 3 cartas.

### Fase 4 — Poderes e equilíbrio

- Implementar os poderes das 12 cartas da seção 6. As outras 10 cartas dos Arcanos Maiores ficam para depois.
- Ajustar valores para que nenhuma combinação quebre o jogo (ex.: pulo duplo + flutuação).
- Tabela de testes das combinações mais comuns, sempre com a Força na 1ª posição.

**Pronto quando:** cada poder funciona e é perceptível ao jogar.

### Fase 5 — Frase final e vocabulário de tarot

- Escolher fontes de vocabulário (sites ou APIs conhecidas de tarot) e verificar disponibilidade e licença de uso.
- Baixar o vocabulário uma vez e guardar em arquivo local, para o jogo funcionar offline e não depender de API durante a corrida.
- Gerador de frases por modelos de texto: combina as cartas sorteadas com faixas de pontuação (corrida curta, média, longa).
- Tela final com a frase, as cartas e a pontuação.

**Pronto quando:** toda corrida termina com uma frase coerente com as cartas e o desempenho.

### Fase 6 — Polimento para celular

- Interface: menu, pausa, ajustes, áreas seguras em telas com notch.
- Som, vibração opcional e animações de carta.
- Funcionar offline (PWA) e desempenho em aparelhos modestos.
- Testes em Android e iPhone.

**Pronto quando:** roda bem em pelo menos 2 aparelhos diferentes.

### Fase 7 — Publicação

- Publicar no GitHub Pages.
- Créditos e licenças no README e no próprio jogo.
- Recorde guardado no aparelho e botão de compartilhar o resultado.

**Pronto quando:** qualquer pessoa abre o link no celular e joga.

## 5. Pontos em aberto

- Quais são os obstáculos finais? A demo usa pedras, troncos com galhos e inimigos (um tipo de monstro roxo), só como exemplo.
- Que inimigos existem e como eles atingem a personagem?
- Confirmar os valores provisórios da demo: moeda comum 10 pontos, dourada 25 e estrela 5.
- A versão completa terá o dash do Carro com toque duplo? A demo só tem a velocidade.
- A frase final com vocabulário de tarot ainda não está na demo.
- A personagem inclina acompanhando a ladeira ou fica sempre reta? E ela balança de leve ao levitar?
- O gesto das mãos (mudra) fica como um círculo pequeno ou ganha mais detalhe?
- Quais fontes de vocabulário de tarot usar, e se há limite de uso ou exigência de crédito.

## 6. Cartas iniciais (12)

Modelo atual das cartas, em ordem de arcano. Os valores são sugestões e serão ajustados na Fase 4.

| Nº | Carta | Poder | Como funciona |
|----|-------|-------|---------------|
| 0 | O Louco | Pulo duplo | Um pulo extra no ar. |
| I | O Mago | Ímã | Atrai moedas e estrelas próximas. |
| II | A Sacerdotisa | Intuição | Segurar o toque desacelera o tempo por 2 s (recarrega). |
| III | A Imperatriz | Vida x2 | Aguenta uma batida. |
| VII | O Carro | Arrancada | Mais velocidade e dash com toque duplo, que atravessa um obstáculo. |
| VIII | A Força | Pulo maior | +35% de altura no pulo. Aparece em 90% das corridas como 1ª carta. |
| IX | O Eremita | Flutuação | Segurar no ar faz a personagem planar. |
| X | A Roda da Fortuna | Sorte | Moedas douradas com o dobro de chance. |
| XIII | A Morte | Renascimento | Volta uma vez depois de bater, com 3 s de invulnerabilidade. |
| XVI | A Torre | Relâmpago | Limpa os obstáculos da tela, 1 vez por corrida. |
| XVIII | A Lua | Noite eterna | Menos visão, pontuação x1,5. |
| XIX | O Sol | Escudo solar | Absorve 1 batida e recarrega em 20 s. |

## 7. Personagem: Sanira

**Pose e movimento:** sentada em posição de ioga (lótus), levitando, vista de frente (virada para a tela), como na foto de referência. Ela desce a ladeira sem pernas correndo. Mãos apoiadas nos joelhos.

**Aparência:**
- Pele marrom e cabelo curto cacheado.
- Olhos fechados, leve sorriso e pés descalços.
- Camiseta preta de manga longa com gola alta, e calça preta.
- Uma faixa em cada manga e um logo em V no centro da camiseta. Essas três partes mudam de cor conforme o poder sorteado. Na maioria das vezes ficam **laranja**, porque a Força aparece em 90% das corridas.

**Aura:**

| Situação | Aura |
|----------|------|
| Força ativa | Laranja, grossa, em volta da personagem. |
| Sem a Força | Fina, cinza clara. |

**Rosto triste:** olhos fechados com sobrancelhas inclinadas, boca para baixo e uma lágrima pequena. Dura 0,5 s ao bater, cair em um buraco ou ser atingida por um inimigo.

**Arquivos de arte (SVG):**

| Arquivo | Para que serve |
|---------|----------------|
| `assets/sanira/sanira-frente-modular.svg` | Arquivo para usar no jogo. Tem camadas separadas: `aura-forca`, `aura-normal`, `rosto-feliz`, `rosto-triste` e `personagem`. |
| `assets/sanira/sanira-frente-forca.svg` | Estado pronto: aura laranja, rosto feliz. |
| `assets/sanira/sanira-frente-sem-forca.svg` | Estado pronto: aura fina cinza, outra cor de poder (exemplo azul). |
| `assets/sanira/sanira-frente-triste.svg` | Estado pronto: rosto triste. |
| `assets/sanira/sanira-frente-previa.png` | Prévia dos três estados lado a lado. |
| `tools/gerar_sanira.py` | Gera os SVGs. Serve para ajustar cores e detalhes. |

**Como o jogo usa o SVG modular:**
- A cor do poder é a variável `--poder`, definida no topo do arquivo.
- Para trocar de cor no canvas, altere o valor de `--poder` no texto do SVG antes de carregá-lo como imagem, ou gere uma imagem pronta por cor.
- Para trocar aura e rosto, mostre ou esconda as camadas pelo `id`.

## 8. Cena de referência

Imagem de como o jogo fica em paisagem (`assets/cena/cena-referencia.png`, com a fonte em `assets/cena/cena-referencia.svg`):

- **Cenário:** céu limpo com sol, montanhas com neve ao fundo em tons suaves, e uma ladeira verde descendo da esquerda para a direita.
- **Personagem:** a Sanira com a aura laranja, levitando um pouco acima da ladeira, no lado esquerdo da tela.
- **Obstáculos de exemplo:** duas pedras e um tronco com galhos no caminho.
- **Moeda:** uma moeda dourada no fim do caminho, à direita.
- **HUD:** contador de pontos no canto superior direito, mostrando 32 pontos.

A tela de cartas (grid 3x4) está publicada em https://claude.ai/artifact/Enejr7zk9hiSUzt8DchrAt.

## 9. Cores dos poderes

Cada poder tem uma cor, usada nas faixas das mangas e no V do peito da personagem. As cores foram escolhidas para aparecer bem sobre o preto da camiseta. A Força é laranja e aparece em 90% das corridas, então o laranja é a cor mais vista.

| Nº | Carta | Poder | Cor | Hex |
|----|-------|-------|-----|-----|
| 0 | O Louco | Pulo duplo | Ciano | `#5FCFE0` |
| I | O Mago | Ímã | Roxo | `#A78BDB` |
| II | A Sacerdotisa | Intuição | Verde | `#6CC38A` |
| III | A Imperatriz | Vida x2 | Rosa | `#F28FB1` |
| VII | O Carro | Arrancada | Turquesa | `#3FBFA8` |
| VIII | A Força | Pulo maior | Laranja | `#F28C28` |
| IX | O Eremita | Flutuação | Azul | `#5B8DEF` |
| X | A Roda da Fortuna | Sorte | Lima | `#B5D96B` |
| XIII | A Morte | Renascimento | Magenta | `#D95FD0` |
| XVI | A Torre | Relâmpago | Vermelho | `#E8604C` |
| XVIII | A Lua | Noite eterna | Prata | `#E6E9F0` |
| XIX | O Sol | Escudo solar | Amarelo | `#F3C74F` |

**Observações:**
- Ciano e turquesa, verde e lima, e rosa e magenta são parecidos. Se ficar difícil distinguir no jogo, trocar um tom de cada par.
- **Regra das 3 cartas:** o V do peito mostra a cor da carta principal (a 1ª) e cada faixa de manga mostra a cor de uma das outras duas cartas.

## 10. Demo (branch `demo`)

**Arquivo:** `demo/index.html`, um arquivo só, sem dependências. Abre direto no navegador ou pelo GitHub Pages. Link de teste: https://claude.ai/artifact/F5B61qTFBcqvcTFKveL7jm

**Como funciona:**
- **Tiragem:** 3 cartas com a Força em 90% das vezes como 1ª. O V do peito usa a cor da 1ª carta e cada manga usa a cor de uma das outras duas. A aura é laranja se a Força estiver nas cartas e fina cinza se não estiver.
- **Controles:** toque em qualquer lugar da tela para pular. O botão "PULAR" é só uma indicação visual. Segurar o toque vale para a Sacerdotisa e para o Eremita. Se a Torre estiver nas cartas, aparece o botão "⚡ RAIO". No computador: barra de espaço pula e a tecla T usa o relâmpago.
- **Fase:** 10 moedas (comum vale 10 pontos, dourada 25), 4 estrelas (5 pontos cada, não contam para o fim) e 6 obstáculos: 2 pedras, 2 troncos com galhos e 2 inimigos, que vêm mais rápido.
- **Fim:** a corrida termina quando as 10 moedas passam (coletadas ou perdidas) ou quando ela cai. A tela final mostra pontos, moedas, estrelas, batidas e os poderes usados, com o que cada um fez.
- **Vida:** 1 vida. Ao ser atingida, o rosto fica triste por 0,5 s e ela fica invulnerável por 1 s.

**Poderes na demo:** os 12 estão implementados. Diferenças em relação à seção 6:

| Carta | Na demo |
|-------|---------|
| O Carro | Só velocidade +25%. O dash com toque duplo ficou de fora. |
| O Eremita | Planar com limite de 1,5 s por pulo. |
| A Torre | Ativada por você, tocando no botão ⚡. Limpa os obstáculos da tela, 1 vez por corrida. |
| O Mago | Atrai moedas e estrelas. |
| A Roda da Fortuna | As moedas douradas passam de 2 para 4 entre as 10. |

**Testes feitos:** 20 verificações automáticas em um navegador de teste (Chromium), todas passaram. Cobrem o pulo duplo do Louco e a recarga, a câmera lenta da Sacerdotisa, o renascimento da Morte, a ordem Sol, Imperatriz e Morte absorvendo batidas, o pulo da Força (+35%), o planar do Eremita, a velocidade do Carro, as moedas douradas da Roda, o bônus da Lua, o relâmpago da Torre e uma corrida completa com 10 moedas e 4 estrelas. Ainda não foi testada em um celular de verdade.

**Fora da demo:** buracos, frase final com vocabulário de tarot, dash do Carro, tipos variados de inimigo e som.
