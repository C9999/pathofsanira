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


## Decisões consolidadas — regras definidas pelo usuário

> Esta seção registra as decisões mais recentes e prevalece sobre descrições antigas ou provisórias das seções anteriores. Valores ainda não definidos permanecem identificados como pendentes.

### 1. Estrutura da corrida e dificuldade

- **Versão final:** a corrida será infinita (endless).
- **Versão de testes atual:** manter a duração/estrutura limitada que já existe, sem transformar os testes em corrida infinita ainda.
- **Fim da corrida:** acontece quando Sanira morre. A tela/estado de fim será chamado **“Meditação interrompida”**.
- **Dificuldade progressiva:** aumentar a frequência dos obstáculos e a velocidade do jogo. A progressão de velocidade (item B da decisão) só começa quando a corrida alcançar o **nível 3**. O sistema de níveis e seus critérios ainda precisam ser especificados.
- **Velocidade:** haverá um limite máximo; o valor ainda será definido.
- **Pausa:** permitida apenas uma vez por corrida. A sessão de jogo será chamada **“Sessão de meditação”**.
- **Geração de percurso:** na versão final, o caminho será procedural e diferente a cada corrida. Nos testes, manter uma quantidade razoável de elementos semelhante à atual.

### 2. Obstáculos, armadilhas e inimigos

- Manter os obstáculos existentes e acrescentar **inimigos voadores** e **armadilhas de chão falso/buracos**.
- Inimigos definidos:
  - **Jacaré:** movimenta-se horizontalmente.
  - **Gado:** permanece parado; é um obstáculo um pouco alto por causa dos chifres.
  - **Tucano:** inimigo voador.
- Cada inimigo permanece na tela seguindo seu comportamento padrão; não terá perseguição ou mudança de comportamento adicional definida por enquanto.
- **Qualquer contato com obstáculo ou inimigo causa dano.**
- Ao receber dano, Sanira fica invulnerável por **1 segundo** (manter o valor atual da demo) e apresenta a expressão triste por **1,5 segundo**.
- **Queda em buraco/armadilha:** não causa morte imediata. Sanira reaparece um pouco antes no percurso, com invulnerabilidade, e pode tentar pular novamente. A queda conta como um dano normal de obstáculo e reduz a vida conforme as regras gerais.

### 3. Sonhos e pontuação

- Não haverá moedas.
- O item coletável será uma **estrela vermelha**, chamada **Sonho**.
- Cada estrela vermelha vale **10 Sonhos**.
- Não haverá bônus adicionais definidos por enquanto.
- A quantidade de Sonhos/estrelas por percurso será mantida razoável, como na demo de testes. Na versão final, a distribuição será procedural.
- **Recorde/resultado dos jogadores:** serão cinco jogadores. A possibilidade considerada é registrar os resultados em uma planilha do Google Drive/Google Sheets; a integração e a estrutura da planilha ainda precisam ser definidas. Não implementar ranking online ou contas sem nova decisão.

### 4. Sorteio das cartas

- As três cartas não podem se repetir na mesma corrida.
- Manter a regra já definida para a primeira carta: A Força aparece em 90% das corridas; nos outros 10%, uma das outras cartas é escolhida uniformemente.
- **Restrição de combinação:** A Lua nunca pode ser sorteada junto com O Sol.
- **Horário da Lua:** deseja-se aumentar em 40% a chance de A Lua ser sorteada quando a pessoa jogar entre **21h e 6h**. A forma exata de aplicar esse aumento (40% relativo ou pontos percentuais) e o ajuste das probabilidades para manter um sorteio válido ainda precisam ser especificados.
- A seleção continua sem repetição e respeitando a restrição Lua + Sol.

### 5. Poderes e vida

Os poderes podem ser ajustados durante o balanceamento. Por enquanto, manter os valores atuais da demo, exceto pelas alterações explicitadas abaixo.

| Carta | Regra definida |
|---|---|
| O Louco | Mantém o pulo duplo. |
| O Mago | Mantém o ímã para atrair itens coletáveis. |
| A Sacerdotisa | Permite evitar **duas** quedas em buracos ou armadilhas de chão por corrida. Substitui a câmera lenta descrita anteriormente. |
| A Imperatriz | Mantém o efeito defensivo de vida extra; pode acumular com os outros poderes defensivos. |
| O Carro | Apenas aumenta a velocidade. **Não terá dash**. |
| A Força | Define a vida inicial: com A Força ativa, Sanira começa com **3 níveis de vida**; sem A Força, começa com **1 nível**. Cada colisão/dano reduz um nível. A Força deixa de ser descrita como poder de pulo maior. |
| O Eremita | Mantém a capacidade de planar por até **1,5 segundo por pulo**. |
| A Roda da Fortuna | Manter o funcionamento atual por enquanto; valores podem ser ajustados no balanceamento. |
| A Morte | Mantém o renascimento/retorno após receber dano, conforme a implementação atual; pode acumular com outros poderes defensivos. |
| A Torre | Ao ativar, limpa **todos os obstáculos** da tela. |
| A Lua | Reduz a visibilidade e multiplica a pontuação por **1,5**. Não pode aparecer junto com O Sol. |
| O Sol | Seu efeito passa a reduzir pela metade o dano de colisão; substitui o escudo que absorvia uma batida e recarregava. |

- Poderes defensivos podem acumular entre si (por exemplo, Imperatriz, Morte e Sol), respeitando seus efeitos individuais.
- Poderes ativos terão um **botão de ativação na região central da tela**. A posição e o comportamento visual exatos serão definidos na implementação.
- Os poderes podem ser reequilibrados futuramente; não tratar os valores atuais como definitivos.

### 6. Sanira e animações

- Sanira acompanha a inclinação da ladeira.
- Manter o movimento suave de levitação.
- Manter o desenho atual das mãos/mudra, sem alterações por enquanto.
- A expressão triste após dano dura **1,5 segundo** e depois retorna à expressão normal.
- Não alterar a animação de pulo atual.
- A aura permanece:
  - **Com A Força:** laranja e mais evidente.
  - **Sem A Força:** cinza clara e fina, como já implementado.

### 7. Mundos e progressão visual

A progressão visual desejada para os ambientes é:
1. Plano/planície verde.
2. Floresta densa.
3. Neve.
4. Fábricas.
5. Vulcão.
6. Espaço.
7. Outra dimensão.

A transição, duração e relação desses ambientes com os níveis de dificuldade ainda serão definidas.

### 8. Tarot, resultado e compartilhamento

- A frase de encerramento será baseada nas **cartas sorteadas e na pontuação**.
- A tela final deverá mostrar as cartas, a pontuação, o resultado da sessão e uma frase.
- O usuário pretende reunir referências de Tarot para decidir como implementar a linguagem e a apresentação das cartas.
- A escolha do baralho/sistema visual (por exemplo, Marselha ou Rider-Waite) continua **em aberto** e depende dessa pesquisa.
- Incluir opção de compartilhar o resultado, como imagem ou texto; formato final ainda a definir.

### 9. Menu, tiragem e início da sessão

- A tela inicial terá o logo com o nome **Path of Sanira**.
- Ao tocar em qualquer lugar da tela inicial, o jogo sorteia as três cartas.
- As cartas serão reveladas uma por uma, com uma animação mais lenta que a versão atual.
- Após a revelação, exibir o botão **“Começar a meditar”**.
- Ao iniciar, Sanira permanece parada na tela por **5 segundos**; somente depois começa a se mover e a corrida efetivamente começa.
- Manter a tiragem de cartas com revelação individual, uma carta por vez.

### 10. HUD, áudio, vibração e orientação

- O HUD deverá exibir pontuação, itens coletados, vida e poderes/habilidades ativos.
- O jogo terá áudio (música/ambiente e efeitos sonoros a definir).
- Terá vibração/háptica.
- A orientação paisagem será obrigatória.

### Lembretes e pendências para decisões futuras

- [ ] **Retomar a regra de dificuldade no nível 3:** definir como os níveis são alcançados e quais mudanças acontecem em cada nível. A progressão de velocidade só começa no nível 3.
- [ ] Definir o limite máximo de velocidade.
- [ ] Definir a integração com Google Sheets para registrar os resultados dos cinco jogadores.
- [ ] Definir como o aumento de 40% na chance da Lua entre 21h e 6h será calculado.
- [ ] Definir os detalhes do sistema de vida e como os efeitos defensivos acumulados interagem.
- [ ] Pesquisar referências de Tarot e escolher o baralho/sistema visual.
- [ ] Definir como a sequência de ambientes se relaciona com níveis, duração e geração procedural.
- [ ] Definir o formato de compartilhamento do resultado.
- [ ] Definir os detalhes de áudio e vibração.


### 11. Status de implementação — versão de testes atual (branch `main`)

> Status conferido no código de `index.html` da branch `main`. **Implementado** significa que existe no protótipo atual; não significa necessariamente que já segue a regra final consolidada. Quando o comportamento da demo divergir da decisão mais recente, isso fica indicado como implementação antiga a substituir.

#### Base do jogo e controles

- [x] Página HTML com canvas e loop de jogo.
- [x] Nome Path of Sanira exibido na tela inicial.
- [x] Personagem levitando em posição de lótus, com SVG e variações de aura/expressão.
- [x] Cenário de ladeira com deslocamento e inclinação.
- [x] Toque/clique durante a corrida faz Sanira pular.
- [x] Suporte a teclado para testes (barra de espaço).
- [ ] Orientação paisagem obrigatória com aviso de rotação.
- [ ] Pausa de uma vez por corrida / “Sessão de meditação”.
- [ ] Corrida infinita na versão final (a demo ainda é limitada).

#### Tiragem e cartas

- [x] Tiragem de três cartas.
- [x] A Força é a primeira carta em 90% dos sorteios.
- [x] Cartas sorteadas sem repetição.
- [x] Revelação individual das cartas com animação escalonada.
- [ ] Regra que impede A Lua e O Sol de saírem juntos.
- [ ] Aumento de 40% na chance da Lua entre 21h e 6h.
- [ ] Revelação mais lenta conforme a nova decisão.
- [ ] Tela inicial que inicia a tiragem ao tocar em qualquer lugar (hoje há botão “Tirar as cartas”).
- [ ] Botão com o texto “Começar a meditar”.
- [ ] Espera de 5 segundos com Sanira parada antes do início efetivo da corrida.

#### Corrida, obstáculos e dano

- [x] Percurso de teste com sequência limitada de elementos.
- [x] Obstáculos de pedra e tronco.
- [x] Inimigo genérico desenhado na demo.
- [x] Colisão com obstáculos causa dano.
- [x] Janela de invulnerabilidade após dano (os tempos variam conforme o efeito defensivo).
- [ ] Geração procedural de percurso para a versão final.
- [ ] Inimigos específicos: jacaré horizontal, gado parado e tucano voador.
- [ ] Inimigos voadores com comportamento próprio.
- [ ] Buracos/armadilhas de chão falso e retorno a um ponto anterior após a queda.
- [ ] Regra final de dano para todos os tipos de contato, integrada ao sistema definitivo de vida.
- [ ] Expressão triste por 1,5 segundo (a demo ainda usa 0,5 segundo).
- [ ] Encerramento por morte com o nome “Meditação interrompida” (a demo ainda encerra ao resolver a sequência de itens ou cair).

#### Coletáveis, pontuação e HUD

- [x] Contador de pontos.
- [x] Coleta de estrelas e moedas na demo.
- [x] HUD mostra as cartas/poderes ativos.
- [ ] Substituir moedas e estrelas atuais por estrelas vermelhas chamadas **Sonhos**.
- [ ] Cada Sonho valer 10 Sonhos.
- [ ] Exibir vida no HUD de acordo com a regra final.
- [ ] Registrar resultados dos cinco jogadores em Google Sheets.
- [ ] Compartilhar o resultado da sessão.

#### Poderes — implementação atual versus regra definida

| Carta | Status no código atual |
|---|---|
| O Louco | [x] Pulo duplo implementado. |
| O Mago | [x] Ímã que atrai moedas/estrelas implementado; ajustar a terminologia e o coletável final. |
| A Sacerdotisa | [ ] O código tem câmera lenta ao segurar o toque; **não corresponde** à nova regra de evitar duas armadilhas. |
| A Imperatriz | [x] Vida extra implementada na demo; conferir e adaptar ao sistema final de níveis de vida. |
| O Carro | [x] Aumento de velocidade implementado; dash não existe. |
| A Força | [ ] O código aumenta a altura do pulo em 35%; **não corresponde** à nova regra de começar com 3 níveis de vida. |
| O Eremita | [x] Planar por até 1,5 segundo por pulo implementado. |
| A Roda da Fortuna | [x] Aumenta a quantidade/chance de moedas douradas na demo; adaptar ao sistema de Sonhos, se aplicável. |
| A Morte | [x] Renascimento uma vez após dano, com invulnerabilidade, implementado. |
| A Torre | [x] Botão de ativação e limpeza dos obstáculos visíveis implementados. |
| A Lua | [x] Redução de visibilidade e multiplicador de pontuação x1,5 implementados; falta a regra de horário e a restrição com O Sol. |
| O Sol | [ ] O código atual usa escudo que absorve uma batida e recarrega; **não corresponde** à nova regra de reduzir o dano pela metade. |

#### Sanira, interface e apresentação

- [x] Aura laranja quando A Força está presente e aura cinza fina quando não está.
- [x] Expressão triste e retorno à expressão normal (duração atual de 0,5 segundo).
- [x] Inclinação da personagem acompanhando a ladeira.
- [x] Arte atual das mãos/mudra mantida.
- [ ] Movimento de levitação refinado conforme a decisão final, se necessário.
- [ ] Menu inicial com logo e fluxo de início conforme as novas regras.
- [ ] Tela final com o título “Meditação interrompida”, cartas, pontuação e frase.
- [ ] Frase gerada com base nas cartas e na pontuação.
- [ ] Botão/ação para compartilhar resultado.
- [ ] Áudio (ambiente/música e efeitos).
- [ ] Vibração/háptica.
- [ ] Botão central para poderes ativos, conforme a nova decisão (a demo tem botão específico da Torre, não um controle central genérico).

#### Mundos e publicação

- [ ] Planície verde, floresta densa, neve, fábricas, vulcão, espaço e outra dimensão como progressão de ambientes.
- [ ] Transições entre mundos.
- [ ] PWA e funcionamento offline.
- [ ] Testes em aparelhos Android e iPhone reais.
- [ ] Integração de placar/registro externo para os cinco jogadores.

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

## 12. Versão paralela V2 — `V2/V2.html`

- A página `V2/V2.html` é uma cópia independente do protótipo `index.html`, criada para testar as decisões mais recentes sem alterar a experiência da página original.
- Título da página: **v 0.2 — Path of Sanira — V2**. A versão principal `index.html` permanece em v0.1.
- Tecnologia mantida: HTML5, Canvas 2D, JavaScript e CSS, sem frameworks ou dependências externas.
- APIs nativas usadas na V2: Web Audio API para efeitos sonoros sintetizados; Vibration API para retorno háptico; Web Share API para compartilhar o resultado, com cópia para a área de transferência como alternativa quando disponível.
- Regras já incorporadas na V2:
  - Toque em qualquer ponto do menu inicia a tiragem; cartas reveladas individualmente em ritmo mais lento; botão “Começar a meditar”.
  - Contagem regressiva de 5 segundos antes do início do movimento.
  - A Força define 3 níveis de vida; sem A Força, 1 nível. A Imperatriz acrescenta um nível.
  - A Sacerdotisa evita duas quedas em buracos; outras quedas causam dano e permitem retornar um trecho do percurso para tentar novamente.
  - O Sol reduz o dano de cada colisão pela metade.
  - Invulnerabilidade de 1 segundo após dano e expressão triste por 1,5 segundo.
  - Restrição que impede A Lua e O Sol de serem sorteados juntos; aumento relativo de 40% no peso de sorteio da Lua entre 21h e 6h.
  - Coletáveis convertidos em estrelas vermelhas chamadas Sonhos, cada uma valendo 10 Sonhos; O Mago atrai Sonhos e A Roda aumenta a quantidade de oportunidades.
  - Inclusão de jacaré móvel, gado parado, tucano voador e buracos/armadilhas, além dos obstáculos já existentes.
  - Pausa permitida uma vez por corrida; botão central para ativar A Torre.
  - HUD com pontos, Sonhos, vida e cartas; encerramento por morte com “Meditação interrompida”.
  - Compartilhamento de resultado, efeitos sonoros simples e vibração, quando suportados pelo navegador/aparelho.
- Limitações ainda presentes na V2:
  - A corrida continua limitada para testes e termina após a coleta de 10 Sonhos; ainda não é endless.
  - A distribuição do percurso continua baseada em uma sequência de teste, não em geração procedural.
  - A progressão de velocidade a partir do nível 3 e os sete mundos ainda não foram implementados.
  - Os efeitos sonoros são sintetizados e pontuais; música/ambiente contínuo ainda não foi criado.
  - A frase final baseada nas cartas e pontuação ainda está pendente.
  - A integração com Google Sheets, o registro dos cinco jogadores e os testes em aparelhos reais continuam pendentes.
  - A orientação paisagem já é exigida pelo aviso de rotação do protótipo; ainda precisa de validação em dispositivos.
- A V2 é uma área de experimentação. Não copiar automaticamente suas alterações para `index.html`; primeiro validar a jogabilidade e depois decidir o que será promovido para a versão principal.

## 13. Ajuste de geração aleatória e remoção temporária de buracos — V2

- Versão atual da página V2 após estes ajustes: **v 0.4**.

- Na V2, inimigos e obstáculos agora são sorteados a cada nova sessão: tanto o tipo de elemento quanto sua posição/distância no percurso variam entre partidas.
- O gerador de testes mistura pedras, troncos, jacarés, gado, tucanos e o inimigo genérico já existente. A quantidade de elementos continua limitada para teste; isso ainda não é a geração procedural infinita da versão final.
- Os Sonhos também recebem posições aleatórias; A Roda aumenta a quantidade de Sonhos extras.
- **Buracos e armadilhas de chão foram removidos temporariamente da V2**, incluindo desenho e colisão. A regra da Sacerdotisa para evitar duas quedas fica sem aplicação prática enquanto não houver armadilhas.
- A decisão geral de gameplay sobre buracos permanece registrada como ideia futura, mas não deve aparecer no protótipo até nova orientação.
- Página alterada: `V2/V2.html`. A página principal `index.html` permanece inalterada.


## Central de testes — 13/11/2026

- Criada a central `teste.html`, com oito acessos independentes.
- `v0.5.html`: cópia da V2 v0.4, com título atualizado para v0.5. A pasta e o arquivo V2 originais foram preservados.
- Experimentos independentes iniciados em v0.0:
  - `Sanira.html`: personagem, combinações de poderes por caixas de seleção e expressão feliz/triste.
  - `Cartas.html`: catálogo das 12 cartas da versão atual.
  - `Tela.html`: referências visuais das telas já existentes no fluxo de teste.
  - `Inimigos.html`: jacaré, gado, tucano e inimigo genérico; seletor de cenário preparado, opções futuras desabilitadas.
  - `Obstaculos.html`: pedra e tronco; buracos registrados como temporariamente removidos.
  - `Tiragem.html`: prévia independente de modal com mensagem de Tarot após o fim da meditação.
  - `Ranking.html`: protótipo visual com dados fictícios; sem integração ou persistência.
- Cada experimento possui HTML próprio e não altera o jogo principal.
- `index.html` (v0.1) e `V2/V2.html` (v0.4) permanecem preservados.
- A página `v0.5.html` é uma cópia do estado atual da V2; não representa ainda novas mecânicas de gameplay.


## Ajustes da central de testes — 13/11/2026

- `Sanira.html`:
  - Lista dos poderes atualizada para refletir nome, descrição e cor definidos na constante `CARDS` do jogo.
  - A cor de cada carta aparece ao lado do poder.
  - Limite de seleção: no máximo três poderes simultâneos; ao atingir três, os demais controles ficam desabilitados até desmarcar algum.
  - Mantida a seleção independente da expressão feliz/triste.
- `Cartas.html`:
  - Catálogo alinhado exatamente à constante `CARDS` da versão jogável `v0.5.html`, preservando ordem, numeração, nomes, poderes, descrições e cores.
- `Inimigos.html`:
  - Incluída uma cena em Canvas com jacaré, gado, tucano e inimigo genérico.
  - Os desenhos usam as mesmas funções de renderização da versão jogável; posições fixas apenas para visualização do catálogo.
- Removido `V2/V2.html`: redundante após a criação da central de testes e da página `v0.5.html`.
- `v0.5.html` e `index.html` permanecem preservados.

## Política de versões e commits — central de testes

- Toda alteração solicitada em uma página da central de testes deve gerar uma nova versão daquela página, incrementando sua numeração independentemente das demais.
- O prefixo de versão deve ser atualizado no início da tag `<title>` do HTML.
- Cada componente mantém sua própria sequência de versões. Exemplo de histórico: `Sanira.html` v0.0 → v0.1 → v0.2; `Cartas.html` v0.0 → v0.1; `Inimigos.html` v0.0 → v0.1. `Obstaculos.html` e os demais experimentos seguem suas próprias numerações.
- As versões anteriores ficam preservadas no histórico do Git; não é necessário criar cópias adicionais de cada HTML para cada incremento.
- Cada página de componente alterada deve receber um commit próprio na branch `main`, com mensagem que identifique o componente e a alteração.
- Quando uma solicitação alterar mais de um componente, fazer commits separados por página.
- Atualizações deste documento devem ser registradas em commit próprio, separado dos commits dos componentes.
- Alterações nos componentes não são aplicadas automaticamente ao jogo integrado. A promoção para o jogo de testes atual (`v0.5.html`) só ocorre quando o usuário solicitar a integração.
- Cada integração deve gerar um novo arquivo/versão do jogo, preservando a versão integrada anterior.
- A página original `index.html` permanece preservada e não deve ser alterada sem solicitação explícita.


## Propostas de poderes em teste — 13/11/2026

As alterações abaixo foram aplicadas somente aos componentes isolados `Cartas.html` e `Sanira.html`. São propostas em avaliação e **não estão aprovadas para integração no jogo**. Não alterar `v0.5.html`, `index.html` ou a lógica integrada dos poderes até aprovação explícita do usuário após os testes.

| Carta | Proposta para avaliação |
|---|---|
| O Louco | No segundo pulo, Sanira executa rapidamente um giro de 360°. |
| A Roda da Fortuna | Cada Sonho coletado vale 1,5. |
| A Morte | Quando Sanira perde todas as vidas, recebe uma vida extra e fica totalmente cinza. |
| O Sol | Reduz em 50% o dano recebido em colisões com inimigos. |

- `Cartas.html` foi atualizado para v0.1 com as novas descrições.
- `Sanira.html` foi atualizado para v0.1 com as mesmas descrições e controles de simulação visual para o giro do segundo pulo (O Louco) e o estado cinza após renascimento (A Morte).
- As simulações em `Sanira.html` são demonstrações visuais do componente; não implementam a lógica de jogo nem alteram a versão integrada.
- A descrição do Sol nesta proposta especifica colisões com inimigos. O escopo de outros tipos de colisão deve permanecer conforme a regra integrada atual até que a proposta seja aprovada ou ajustada.

## Idioma dos commits

- Todas as mensagens de commit deste repositório devem ser escritas em português, incluindo alterações de código, documentação, correções e manutenção.


## Sacerdotisa em teste — 13/11/2026

- `Sanira.html` atualizado para v0.2 com simulação interativa da Sacerdotisa: proteção automática na próxima colisão simulada com obstáculo, colisão anulada, recarga de 30 segundos com indicador de progresso e aura verde (#6CC38A) por 1,5 segundo após atravessar.
- O teste exige que A Sacerdotisa esteja selecionada. O botão de simulação só fica habilitado quando o poder está carregado.
- `Cartas.html` atualizado para v0.2 para manter a descrição da Sacerdotisa sincronizada com o componente.
- Os testes são experimentos isolados: não alteram `v0.5.html` nem integram a mecânica ao jogo. A integração depende de aprovação explícita após os testes.


## Beta v0.6 — novos poderes e HUD

- Criado `beta.html` como nova página jogável beta, derivada da versão integrada `v0.5.html`; a versão anterior foi preservada sem alterações.
- O HUD da corrida exibe o nome de cada carta acompanhado de sua cor, em vez do nome do poder. A intenção é incentivar os jogadores a memorizar os efeitos das cartas.
- Aplicados na beta os poderes revisados: O Louco gira 360° no segundo pulo; A Sacerdotisa atravessa automaticamente o próximo obstáculo (não inimigos), ativa recarga de 30 segundos com indicador no topo e aura verde por 1,5 segundo; A Roda da Fortuna multiplica o valor dos Sonhos por 1,5; A Morte concede uma vida extra ao zerar as vidas e deixa Sanira totalmente cinza; O Sol reduz em 0,5 o dano somente nas colisões com inimigos.
- A central `teste.html` agora aponta para `beta.html` como jogo atual. `v0.5.html` permanece preservada como versão anterior.


## Beta v0.7 — recarga visual e seleção de poderes para testes

- `beta.html` atualizado para v0.7.
- A Sacerdotisa mantém a proteção automática contra o próximo obstáculo (sem proteger contra inimigos), mas sua recarga foi reduzida de 30 para **15 segundos**.
- Removido o contador separado da Sacerdotisa no HUD. Enquanto recarrega, o espaço da própria carta é ocupado por uma barra horizontal verde, com a mesma largura e altura do indicador da carta; a barra progride até completar. Ao terminar, o nome da carta volta a aparecer.
- O menu da beta oferece dois caminhos: tiragem aleatória, que preserva as regras atuais, e seleção manual para testes.
- A seleção manual permite escolher exatamente três poderes, impede a combinação A Lua + O Sol e inicia a sessão com os poderes selecionados, sem sorteio.
- Ao encerrar a meditação, o botão retorna à tela inicial, permitindo escolher outro modo e reiniciar.
- Componentes isolados atualizados: `Sanira.html` v0.3 (simulação da Sacerdotisa com 15 s), `Cartas.html` v0.3 (descrição revisada) e `Tela.html` v0.1 (fluxo do menu e retorno após a sessão).
- A página `index.html` e a antiga `v0.5.html` permanecem preservadas. Os componentes continuam independentes da beta, exceto pelas alterações explicitamente integradas nesta v0.7.

## Beta v0.8 — modo de tela cheia

- `beta.html` atualizado para v0.8.
- Adicionado botão **“Tela cheia”** à interface da beta, disponível antes e durante a sessão.
- O botão solicita tela cheia para o documento usando a Fullscreen API, com preferência por ocultar a interface de navegação quando o navegador aceitar essa opção.
- O texto do botão acompanha o estado do navegador e permite sair da tela cheia.
- A entrada em tela cheia ocorre após toque/clique do usuário, conforme a exigência dos navegadores móveis.
- Se a API não estiver disponível ou o navegador negar a solicitação, a demo continua funcionando em modo normal.
- A tela cheia não força a orientação do aparelho; a exigência de paisagem continua sendo tratada pelo aviso de rotação existente.


### Beta v0.9 — correção dos controles e tela cheia (16/11/2026)

- Corrigida a falha de JavaScript causada por sequências literais `\\n` inseridas no bloco de script da beta v0.8, que impediam a execução de todo o código e, consequentemente, inutilizavam os botões.
- Normalizadas as quebras de linha no HTML e no JavaScript.
- Botão de tela cheia posicionado explicitamente sobre a interface, com prioridade de camada e interação por toque.
- Camada de aviso de rotação elevada para permanecer acima da interface.
- Validada a sintaxe do JavaScript após a correção com compilação do script.
- Ainda é necessária validação de interação em navegador Android real; o suporte à Fullscreen API depende do navegador e da interação do usuário.


## Beta v0.10 — remoção de tela cheia e integração visual dos inimigos (24/11/2026)

- Removido integralmente o botão de tela cheia da beta, incluindo estilos, eventos e chamadas à Fullscreen API. A experiência volta a depender somente dos controles de toque já existentes.
- Integrados à beta os desenhos de jacaré, gado, tucano e inimigo genérico da branch `inimigos`, mantendo as dimensões de referência e as chamadas de renderização usadas pelos elementos do percurso.
- A beta utiliza o estilo padrão dos desenhos. As variações temáticas continuam disponíveis no componente isolado para avaliação; não foi implementada seleção de estilo dentro da partida.
- Atualizado `Inimigos.html` para v0.1 com galeria de estilos, alternativas visuais e ampliação dos desenhos, derivada do experimento da branch `inimigos`.
- Atualizada a central `teste.html` para indicar beta v0.10 e componente Inimigos v0.1.
- Os SVGs de cartas Tarot e o estudo de geração procedural da branch não foram integrados: são materiais independentes, e o CODEX mantém a escolha da arte das cartas e as regras de geração como decisões em aberto.
- `index.html` e `v0.5.html` permanecem inalterados.


## Atualização — beta v0.11 (24/11/2026)

### Alterações implementadas

- **Tiragem:** as cartas reveladas mostram somente o nome da carta; foram removidos da face revelada o número, o nome do poder, a descrição e os rótulos de posição (V do peito e mangas).
- **O Carro:** aumento de velocidade atualizado de 25% para **40%**.
- **A Morte:** quando concede a vida extra e deixa Sanira totalmente cinza, todos os demais poderes são desativados. O HUD passa a exibir somente A Morte como poder ativo e o aumento de velocidade de O Carro também é encerrado.
- **Início da meditação:** removida a contagem regressiva visual. Após “Começar a meditar”, Sanira fica centralizada, o terreno permanece reto e a sessão imóvel por **3 segundos**. Ao fim da espera, Sanira retorna à posição de jogo, o terreno inclina e o movimento começa.
- **Catálogo Cartas:** atualizado para refletir O Carro +40% e a desativação dos demais poderes pela Morte.

### Versões

- `beta.html`: **v0.11**.
- `Cartas.html`: **v0.4**.
- `teste.html`: central atualizada para exibir as versões acima.
- `index.html` e versões beta anteriores permanecem intactas.

### Commits

- `f285490` — atualiza tiragem, poderes e início da meditação na beta v0.11.
- `b4eacbd` — corrige espera imóvel e desativação completa dos poderes após a Morte.
- `8c43875` — atualiza HUD para refletir poderes desativados pela Morte.
- `42bfc99` — atualiza regras das cartas Carro e Morte.
- `53cb613` — atualiza central para beta v0.11 e cartas v0.4.

- `a80874d` — corrige a descrição da carta O Carro na beta após o ajuste para +40%.

### Validação

- Validar sintaxe JavaScript da beta.
- Confirmar ausência de contagem regressiva e dos rótulos de posição na tiragem.
- Confirmar que a movimentação e inclinação só começam depois dos 3 segundos.
- Teste de gameplay em aparelho físico ainda não realizado.


## Atualização — beta v0.12 (24/11/2026)

### Alterações implementadas

- **A Força:** nome do poder atualizado para **“Sua habilidade principal”** na tiragem e no catálogo de cartas.
- **Tiragem:** cada carta revelada apresenta a barra com sua cor, número, nome e nome do poder. A explicação/descrição do poder não é exibida.
- **HUD inicial:** permanece oculto durante a espera de 3 segundos e continua oculto quando a corrida começa. Aparece no primeiro pulo, uso do raio, dano recebido ou Sonho coletado.
- **Tucano:** altura de voo aumentada em 20 px; a colisão acompanha a nova posição. A intenção de balanceamento é que o pulo simples alcance o tucano e o pulo duplo consiga passar por cima.
- **Término da beta:** adicionado um marco visual “FIM” ao final do percurso. A sessão termina ao alcançar esse marco, em vez de encerrar ao coletar uma quantidade fixa de itens.
- **HUD:** removidos o placar de pontos e o total de Sonhos durante a corrida.
- **Vida:** contador substituído por círculos abaixo das cartas. A Força mostra três círculos laranjas; sem A Força, é exibido o número de vidas inicial correspondente. A Imperatriz acrescenta um círculo rosa. Dano de meia vida é representado por meio círculo. Após o renascimento da Morte, aparece somente um círculo cinza.

### Versões

- `beta.html`: **v0.12**.
- `Cartas.html`: **v0.5**.
- `teste.html`: central atualizada para exibir as versões acima.
- `index.html` e versões beta anteriores permanecem intactas.

### Commits

- `b3b7525` — atualiza tiragem, HUD, vidas, tucano e término da beta v0.12.
- `96f7255` — atualiza nome do poder da Força no catálogo.
- `fe4d004` — atualiza central para beta v0.12 e cartas v0.5.

### Validação

- Sintaxe JavaScript da beta validada.
- Tiragem contém barra de cor, número, nome e nome do poder, sem descrição.
- HUD de pontos e total de Sonhos removidos da tela de jogo.
- HUD condicionado ao primeiro evento de interação definido.
- Marco final e condição de encerramento adicionados.
- Teste de gameplay em aparelho físico ainda não realizado; altura relativa do tucano e a diferença entre pulo simples/duplo precisam de confirmação visual em jogo.


## Atualização — beta v0.13 (24/11/2026)

- Segundo pulo de O Louco ampliado: impulso vertical de 1,5× o pulo normal, para permitir superar o tucano com folga. O pulo normal permanece inalterado.
- Controles de pausa e áudio ficam disponíveis já durante a espera inicial; o controle PULAR também aparece durante esse período visualmente.
- Botão de áudio movido para o canto superior direito, ao lado do controle de pausa, para evitar sair da área visível.
- Adicionado ambiente sonoro meditativo sintetizado pela Web Audio API: camadas suaves de tons graves com pulsação lenta. O controle liga/desliga tanto o ambiente quanto os efeitos sonoros.
- O áudio é iniciado ao começar a sessão, respeitando as restrições de reprodução automática dos navegadores.
- Pausa durante a espera inicial preserva o estado de espera e retoma a contagem corretamente.
- Validação sintática do JavaScript realizada. Não foi realizado teste físico em aparelho.


## Atualização — beta v0.14 (24/11/2026)

- Removido o botão visual “PULAR”. A função de pulo foi mantida: toque na área do jogo e tecla Espaço continuam acionando o pulo, inclusive o pulo duplo de O Louco.
- Removidos o botão de pausa e a tela de pausa; a sessão não oferece pausa nesta versão.
- Removido o botão de áudio da tela de jogo. O ambiente meditativo continua ativo durante a sessão; o controle para ligar/desligar ficará para uma atualização futura da tela de título.
- Corrigido o ambiente sonoro: os tons anteriores eram graves e muito baixos. Agora há camadas de tons senoidais em frequências mais audíveis, com modulação lenta e volume ambiente suave.
- A inicialização do áudio ocorre diretamente no clique/toque de “Começar a meditar”, para atender à política de reprodução dos navegadores.
- JavaScript validado sintaticamente. Não foi realizado teste físico em aparelho.


## Atualização — áudio meditativo e central de músicas (24/11/2026)

- **Beta v0.15:** a música ambiente começa no início do período de espera (`intro`), junto ao início da nova sessão, e é interrompida com transição curta assim que a rodada termina. Na próxima chamada de início, uma nova reprodução começa durante o novo período de espera.
- O áudio contínuo usa Web Audio API e é encerrado por redução gradual de volume e parada dos osciladores; os efeitos sonoros permanecem independentes.
- **Musica.html v0.0:** nova sessão independente na central de testes para comparar cinco ambientes sintetizados: Serenidade original, Jardim Zen, Maré tranquila, Céu estrelado e Floresta interior. A seleção é feita por radio buttons; escolher outra faixa durante a reprodução troca a música imediatamente. Os controles permitem começar e parar a escuta.
- A central de testes passa a apontar a beta v0.15 e inclui o acesso à sessão de músicas.
- A reprodução depende do suporte do navegador à Web Audio API e da interação do usuário para liberar o áudio. A validação auditiva em aparelhos físicos ainda está pendente.


## Atualização — beta v0.16: botão da Torre (24/11/2026)

- O botão de ativação da Torre foi reposicionado para o centro superior da tela de jogo.
- O botão é circular, mede 27 × 27 px (um pouco menor que o diâmetro externo aproximado de 30 px da estrela vermelha Sonho) e exibe somente o símbolo de raio.
- O botão aparece durante a sessão quando A Torre está entre as cartas ativas e ainda não foi utilizada. Ao tocar, ativa o poder, remove os obstáculos visíveis conforme a regra existente e desaparece.
- Se A Morte for ativada, os demais poderes são desativados e o botão da Torre desaparece imediatamente, mesmo que ainda não tenha sido usado.
- O atalho de teclado T continua disponível. A central de testes aponta para a beta v0.16.
- Validação por leitura do código e conferência dos arquivos publicados; teste visual em aparelho ainda pendente.


## Atualização de implementação — 24/11/2026

### Beta v0.17
- O botão ⚡ da Torre fica imediatamente ao lado do mostrador “Torre” no HUD, alinhado verticalmente ao indicador.
- O botão só aparece durante a corrida, depois que o HUD é exibido; permanece oculto na tela inicial, na tiragem e no período de espera antes do início.
- Ao ativar o poder da Torre, o botão desaparece e não retorna naquela sessão.
- O botão também permanece oculto se A Morte desativar os demais poderes.
- A central de testes aponta para a beta v0.17.

### Sessão de músicas v0.1
- A faixa 3, “Maré tranquila”, recebeu vozes triangulares e frequências médias adicionais para melhorar a audibilidade em alto-falantes de celulares.
- As demais quatro faixas permaneceram inalteradas.
- A alteração é um ajuste de síntese; a reprodução ainda precisa ser conferida auditivamente em aparelhos reais.

## Beta v0.18 — arte Tarot na tiragem (26/11/2026)

- Integradas à tela de tiragem as 12 ilustrações SVG do experimento `inimigos/Cartas-Tarot.html`, mantendo a paleta individual de cada carta, moldura e numeração romana.
- Mantidos os nomes e os nomes dos poderes exatamente conforme a constante `CARDS` da beta. As descrições não foram substituídas pelo texto antigo do experimento; a tiragem continua exibindo apenas nome e poder, como na versão anterior.
- A alteração é restrita à tiragem antes da corrida. O HUD, os poderes, a lógica de sorteio e as ilustrações de Sanira permanecem inalterados.
- `beta.html` atualizado para v0.18; `teste.html` atualizado para apontar a nova versão. `index.html` e beta v0.17 preservados no histórico do Git.
- Validação realizada por inspeção do código e conferência da presença das 12 ilustrações SVG. Teste visual e de interação em aparelho real ainda pendente.



## Atualização — beta v0.19: temas aleatórios dos inimigos (26/11/2026)

- Cada inimigo recebe aleatoriamente um dos cinco temas visuais disponíveis para seu tipo no conjunto `THEMES`: Jacaré, Gado, Tucano e inimigo genérico.
- A escolha é feita individualmente quando os inimigos são criados para a sessão; inimigos do mesmo tipo podem aparecer com aparências diferentes na mesma corrida.
- Os temas incluem as variações já desenhadas no experimento: padrão, alternativas de cor/textura e tema inspirado nas cartas.
- Foram preservados os tamanhos, hitboxes, pesos de aparição, movimentos, colisões, dano e regras dos poderes. Rocha e tronco não recebem variação visual.
- `beta.html` atualizado para v0.19 e `teste.html` aponta para a nova versão. A beta v0.18 permanece preservada no histórico do Git.
- Integração realizada por inspeção dos trechos de criação e renderização. Teste visual e de jogabilidade em aparelho real ainda pendente.

## Decisões consolidadas — Etapa 1 (26/11/2026)

As decisões abaixo foram confirmadas pelo usuário e prevalecem sobre qualquer descrição divergente anterior neste documento. Esta atualização é documental: não altera a implementação da beta.

1. **A Sacerdotisa — manter:** protege automaticamente contra o próximo obstáculo; não protege contra inimigos; após ativar, entra em recarga de 15 segundos; exibe aura verde por 1,5 segundo. Não depende de botão. Esta regra substitui descrições antigas sobre câmera lenta ou proteção limitada a quedas em buracos.
2. **Acúmulo de vidas — manter:** A Força define 3 níveis de vida iniciais; sem A Força, Sanira começa com 1. A Imperatriz concede uma vida extra. A Morte concede uma vida extra ao perder todas as vidas.
3. **O Sol — manter:** reduz em 0,5 o dano recebido em colisões com inimigos.
4. **Velocidade máxima e progressão — regra atualizada:** até o nível 3, a velocidade permanece igual. No nível 4, aumenta 15%; no nível 5, recebe mais 15% (total de +30% em relação à velocidade-base). O aumento de 40% de O Carro é somado a esses percentuais quando a carta estiver ativa; portanto, no nível 5 com O Carro, o aumento total é de 70% sobre a velocidade-base. O nível 5 representa o teto da progressão de velocidade definida nesta etapa.
5. **A Lua — manter:** entre 21h e 6h, recebe peso relativo de 1,4 no sorteio, equivalente a um aumento relativo de 40%. A regra de sorteio continua sujeita às demais restrições, incluindo não combinar A Lua com O Sol.
6. **Acúmulo de poderes defensivos — manter:** poderes defensivos podem acumular entre si, respeitando os efeitos individuais de cada carta.
7. **A Força — regra específica confirmada:** como poder da carta, concede apenas 3 níveis de vida. A altura e a mecânica do pulo atual devem permanecer exatamente como estão; esta decisão não autoriza reduzir, aumentar ou modificar o pulo. A descrição da carta não deve mencionar aumento de pulo. Sem A Força, a vida inicial é 1, conforme a regra geral de vidas.
8. **A Imperatriz — manter:** concede uma vida extra.
9. **A Morte — manter:** ao perder todas as vidas, concede uma vida extra; após o renascimento, os demais poderes são desativados.

### Pendências que permanecem

- Definir a integração com Google Sheets para registrar os resultados dos cinco jogadores.
- Definir como o aumento de 40% na chance da Lua entre 21h e 6h será calculado na implementação (o peso relativo de 1,4 já está definido).
- Pesquisar referências de Tarot e escolher o baralho/sistema visual.
- Definir como a sequência de ambientes se relaciona com níveis, duração e geração procedural.
- Definir o formato de compartilhamento do resultado.
- Definir os detalhes de áudio e vibração.
- Validar no código da beta se as regras consolidadas de progressão, vida e poderes já estão implementadas; decisões documentadas não significam implementação concluída.
- Validar no código da beta se todas as regras acima já estão implementadas; decisões documentadas não significam implementação concluída.


## Decisões consolidadas — pendências da Etapa 1 (26/11/2026)

O usuário definiu as quatro pendências restantes da Etapa 1. Esta atualização é documental e não altera o código da beta.

1. **Limite e progressão da velocidade:** até o nível 3, a velocidade permanece igual. No nível 4, aumenta 15%; no nível 5, aumenta mais 15%, totalizando +30% sobre a velocidade-base. Se O Carro estiver ativo, seu bônus de +40% é somado aos aumentos dos níveis. Assim, no nível 5 com O Carro, o aumento total é de +70% sobre a velocidade-base. O nível 5 é o teto da progressão de velocidade definida nesta etapa.
2. **Sistema de níveis e dificuldade:** cada nível deve durar aproximadamente dois minutos de jogo. A geração de inimigos e obstáculos permanece aleatória. No nível 4, a ocorrência de inimigos e obstáculos aumenta em 10%; no nível 5, aumenta em 20%. Esses percentuais descrevem o ajuste de dificuldade de cada nível, não uma sequência de bônus a somar entre os níveis.
3. **Acúmulo de poderes defensivos:** manter o funcionamento atual, já testado extensivamente pelo usuário. Não alterar a interação existente nesta etapa.
4. **Regra de dano e vidas:** manter a regra atual consolidada, sem alterações nesta etapa.

### Observações para implementação futura

- A duração de aproximadamente dois minutos por nível é uma meta de tempo de jogo, não uma garantia exata; a geração de elementos continua aleatória.
- A implementação deverá aplicar os aumentos de velocidade e de ocorrência de inimigos/obstáculos ao atingir os níveis indicados, preservando o sorteio aleatório dos elementos.
- Estas decisões não autorizam alterar a altura ou a mecânica do pulo.

## Decisões consolidadas — Etapa 2: evolução da corrida (26/11/2026)

As decisões abaixo foram confirmadas pelo usuário e prevalecem sobre descrições anteriores divergentes deste documento. Este registro consolida o planejamento; a implementação na beta será feita em atualização própria.

### 1. Níveis, duração e dificuldade

- A corrida terá cinco níveis.
- Cada nível terá duração aproximada de **dois minutos em tempo real**. O cronômetro continua rodando durante dano, invulnerabilidade e transições. O jogo não terá pausa manual.
- Os níveis 1, 2 e 3 mantêm a velocidade e a frequência-base de obstáculos/inimigos.
- No nível 4, a velocidade aumenta 15% sobre a velocidade-base e a frequência de obstáculos/inimigos aumenta 10%.
- No nível 5, a velocidade total fica 30% acima da velocidade-base e a frequência de obstáculos/inimigos fica 20% acima da frequência-base. Esses valores permanecem fixos durante todo o nível 5, que é infinito; não existe nível 6.
- O bônus de O Carro (+40%) é somado aos bônus de velocidade dos níveis: no nível 5, o total é +70% sobre a velocidade-base.
- A geração continua aleatória. Não serão adicionados novos tipos de inimigos ou obstáculos nesta etapa.
- Os Sonhos mantêm a mesma frequência em todos os níveis.

### 2. Mundos e ordem dos níveis

| Nível | Mundo |
|---|---|
| 1 | Planície verde |
| 2 | Floresta densa |
| 3 | Fábricas |
| 4 | Neve |
| 5 | Espaço sideral |

Esta sequência substitui, para a estrutura de cinco níveis desta etapa, a sequência provisória de ambientes descrita anteriormente. Vulcão e outra dimensão não fazem parte dos cinco níveis agora definidos.

### 3. Estilo visual dos inimigos

O tema visual dos inimigos deixa de ser sorteado individualmente. O nível determina o estilo, para todos os inimigos daquele nível:

| Nível | Estilo dos inimigos |
|---|---|
| 1 | Padrão |
| 2 | Alternativa 1 |
| 3 | Alternativa 2 |
| 4 | Alternativa 3 |
| 5 | Cartas — monocromático |

As variações visuais existentes no conjunto de temas da beta devem ser reaproveitadas e mapeadas para esta progressão. O estilo muda junto com a transição visual do nível. Não alterar comportamento, hitboxes ou dimensões dos inimigos ao trocar o tema.

### 4. Variação visual dos obstáculos

- Nos níveis 1, 2 e 3, rocha e tronco mantêm a aparência atual.
- No nível 4 (Neve):
  - a rocha passa a ter aparência de iceberg;
  - o tronco passa a ter aparência de tronco congelado.
- No nível 5 (Espaço sideral):
  - a rocha passa a ter aparência de pedra espacial/asteroide;
  - o tronco passa a ter aparência de cometa.
- As variações preservam exatamente as dimensões atuais de cada obstáculo, incluindo suas hitboxes.

### 5. Transição entre níveis

A mesma transição será usada em todas as mudanças de nível, inclusive do nível 4 para o 5:

1. No início da transição, interromper imediatamente a geração de novos obstáculos, inimigos e Sonhos.
2. Remover imediatamente todos os obstáculos, inimigos e Sonhos que ainda estiverem na tela ou pendentes no percurso.
3. Manter o percurso reto e vazio por 10 segundos, com Sanira continuando a correr.
4. Fazer uma dissolução visual de 3 segundos do cenário anterior para o cenário do próximo nível.
5. A troca da música acontece simultaneamente à dissolução visual.
6. Após a dissolução, manter o percurso reto e vazio por mais 5 segundos.
7. Ao final dos 5 segundos, retomar a geração aleatória conforme as regras do novo nível.

- Não exibir avisos ou mensagens de mudança de nível.
- Não pausar Sanira durante a transição.
- A dissolução visual escolhida é suave, com o cenário antigo desaparecendo gradualmente enquanto o novo surge.
- A troca de estilo dos inimigos e de aparência dos obstáculos ocorre junto com a mudança de cenário.

### 6. Músicas por nível

Cada nível usa uma das cinco músicas existentes em `Musica.html`, na ordem atual da página:

1. Nível 1 — Serenidade original.
2. Nível 2 — Jardim Zen.
3. Nível 3 — Maré tranquila.
4. Nível 4 — Céu estrelado.
5. Nível 5 — Floresta interior.

A música troca junto com a dissolução visual do cenário. A implementação deverá reutilizar as composições/sínteses existentes, sem alterar a ordem nem substituir as faixas.

### 7. Escopo e estado da implementação

- As decisões acima definem o comportamento desejado, mas não significam que já estejam implementadas na beta.
- A beta v0.19 permanece preservada no histórico.
- A implementação da progressão, dos cenários, das transições, dos temas de inimigos/obstáculos e da seleção musical será registrada em nova versão da beta, com commits separados por página/componente conforme as regras do projeto.
- A página original `index.html` não deve ser alterada.

## Implementação — beta v0.20: progressão de cinco níveis (26/11/2026)

- A beta passa a gerar obstáculos e Sonhos continuamente durante a sessão, sem linha de chegada fixa. A corrida termina quando Sanira morre; o nível 5 não tem limite de duração.
- O cronômetro de cada nível usa tempo real. A transição começa aos 102 segundos e dura 18 segundos (10 segundos de percurso reto e vazio, 3 segundos de dissolução e troca musical, e 5 segundos de percurso reto e vazio), completando ciclos de aproximadamente 120 segundos. O cronômetro continua durante a transição; não há pausa manual.
- No início da transição, a geração é interrompida e todos os obstáculos, inimigos e Sonhos pendentes são removidos. A geração é retomada ao fim dos 5 segundos posteriores à dissolução.
- Cenários integrados na ordem: planície verde, floresta densa, fábricas, neve e espaço sideral. A dissolução combina o cenário anterior e o novo durante 3 segundos.
- As cinco músicas de `Musica.html` foram reutilizadas na ordem existente. A faixa muda junto com a dissolução, com transição gradual de áudio de 3 segundos.
- Os inimigos agora usam o tema correspondente ao nível: padrão, alternativa 1, alternativa 2, alternativa 3 e Cartas monocromático. A escolha deixa de ser aleatória por inimigo.
- Nos níveis 1 a 3, rocha e tronco mantêm a arte original. No nível 4, viram iceberg e tronco congelado; no nível 5, asteroide e cometa. As dimensões e hitboxes permanecem as mesmas.
- A frequência de obstáculos/inimigos é ajustada em +10% no nível 4 e +20% no nível 5; a frequência de Sonhos permanece constante entre níveis.
- Velocidade: base até o nível 3, +15% no nível 4 e +30% no nível 5. O bônus de O Carro (+40%) é somado. O cálculo da velocidade também é reaplicado após o renascimento de A Morte.
- A beta v0.19 permanece preservada no histórico. A central de testes foi atualizada para apontar a v0.20.
- Validação realizada: sintaxe JavaScript aprovada e inspeção dos pontos principais da progressão, transição, áudio, temas e obstáculos. Ainda falta teste visual e de jogabilidade em navegador/aparelho real.

## Publicação da versão principal — v0.19 (26/11/2026)

Por decisão explícita do usuário, a página principal foi atualizada com uma cópia integral da beta v0.19, incluindo os componentes, a arte Tarot da tiragem e os temas visuais aleatórios dos inimigos que faziam parte daquela versão.

- **index.html:** agora contém a versão principal v0.19, com título `v 0.19 — Path of Sanira`.
- **Origem do conteúdo:** beta v0.19 no commit `6eefcf31ace7f1416a6ba931d294c590a2b3a531`.
- **beta.html:** permanece na v0.20 e continua sendo o ambiente de desenvolvimento das novas definições da Etapa 2.
- **teste.html:** continua apontando para a beta v0.20.
- As decisões de níveis, mundos, transições, músicas e variações de obstáculos/inimigos da Etapa 2 serão implementadas e validadas na beta. Não devem ser aplicadas automaticamente à página principal.
- Quando uma nova versão da beta estiver validada e o usuário solicitar sua promoção, a página principal poderá receber uma cópia dessa versão, preservando a versão principal anterior no histórico do Git.
- A versão principal anterior v0.1 permanece recuperável pelo histórico do Git.

Esta publicação substitui a orientação anterior de manter index.html intocada: a página principal agora representa a versão estável promovida pelo usuário, enquanto beta.html concentra o desenvolvimento em andamento.


## Correção — beta v0.21: inicialização da corrida e temas dos inimigos (26/11/2026)

- Corrigida a falha que interrompia o loop de animação logo após o início da corrida. A beta v0.20 fazia referência a `THEMES` e às funções de desenho dos inimigos, mas o bloco que declarava esses temas e renderizadores havia sido perdido durante a implementação da progressão.
- Restaurados na beta os dados dos cinco temas de cada tipo de inimigo (jacaré, gado, tucano e inimigo genérico) e suas funções de desenho, reaproveitados da versão v0.19.
- Com a restauração, a geração inicial de obstáculos deixa de falhar por referência inexistente e o loop pode continuar atualizando a distância, o cenário, os obstáculos e os Sonhos.
- A alteração está restrita a `beta.html`. A página principal `index.html` permanece na v0.19.
- Nova versão da beta: **v0.21**.
- Validação pendente: testar a tiragem, início após os 3 segundos, movimento do percurso, aparecimento de inimigos/obstáculos/Sonhos, colisões e transições em navegador real. A restauração resolve as referências ausentes identificadas no código, mas não substitui o teste de jogabilidade.


## Ajuste temporário — níveis de 30 segundos na beta v0.22 (26/11/2026)

- A duração-alvo dos níveis 1 a 4 foi reduzida temporariamente de aproximadamente 120 para **30 segundos**, para acelerar os testes.
- A corrida normal acontece durante os primeiros **12 segundos**. Em seguida começa a transição já definida, com **10 segundos** de percurso reto e vazio, **3 segundos** de dissolução/troca musical e **5 segundos** adicionais de percurso reto e vazio. Total: 30 segundos por nível.
- O cronômetro geral continua rodando durante a transição. Ao final dos 18 segundos, o cronômetro do nível reinicia.
- O nível 5 continua infinito e não inicia transição para um sexto nível.
- Ajuste restrito a `beta.html`; `index.html` permanece na v0.19.
- Nova versão da beta: **v0.22**.


## Ajuste — beta v0.23: transição inicial de 4 segundos (26/11/2026)

- O primeiro trecho da transição entre níveis foi reduzido de **10 para 4 segundos**.
- Permanecem inalterados os **3 segundos de dissolução visual com troca musical** e os **5 segundos finais** de percurso reto e vazio.
- A transição completa agora dura **12 segundos**. Com os 12 segundos de corrida normal, cada nível de teste dura **24 segundos**.
- O cronômetro geral continua rodando durante toda a transição. Inimigos, obstáculos e Sonhos continuam sem geração durante os três trechos.
- O nível 5 continua infinito e não inicia transição para um sexto nível.
- Alteração restrita à beta; a página principal `index.html` permanece na v0.19.
- Nova versão da beta: **v0.23**.


## Implementação — beta v0.24: encerramento, ranking e controles da tiragem (26/11/2026)

As definições da Etapa 3 foram implementadas na beta, sem alterar a página principal `index.html`.

### Tela de tiragem
- O botão principal agora exibe **“Tirar a sorte através das cartas”**.
- Removido o botão de seleção manual de poderes para teste e seu fluxo associado.
- Adicionado controle de música ligada/desligada no canto inferior direito da tela de tiragem. O padrão é ligado.
- Adicionado botão de tela cheia no canto superior direito. O controle solicita o modo fullscreen do navegador e permite sair dele.

### Encerramento da sessão
- A tela de encerramento apresenta duas colunas: resumo da sessão à esquerda e ranking à direita.
- O resumo mostra **Pontos**, **Tempo meditando**, **Nível** em que a sessão terminou e a quantidade de Sonhos.
- Removidos os indicadores de colisões e vida restante.
- A lista de poderes exibe o nome e somente a descrição do efeito de cada carta; não mostra contagem de usos nem estatísticas de ativação.
- O botão **“Voltar à tela inicial”** fica no rodapé da coluna esquerda.
- O botão **“Compartilhar”** fica no rodapé da coluna direita e compartilha texto com pontuação, tempo, nível e cartas.

### Ranking local
- Cada sessão encerrada é registrada no armazenamento local do navegador (`localStorage`), limitado às 50 melhores entradas.
- Até a futura integração com login Google, o nome exibido é **“Jogador”**.
- Cada linha mostra nome, pontos, tempo em minutos e segundos e as três cartas como bolinhas coloridas.
- A sessão recém-encerrada recebe destaque visual.
- Ordenação: maior pontuação primeiro; em empate, maior tempo de meditação primeiro. O desempate compara o tempo em milissegundos, mesmo que a tela mostre apenas minutos e segundos.
- O ranking é local ao navegador/dispositivo e ainda não sincroniza entre pessoas ou aparelhos. Login Google e ranking online permanecem pendentes.

### Pontuação e dificuldade no nível 5
- A pontuação acumulada continua preservada entre os níveis.
- Após **60 segundos jogados no nível 5**, é aplicado uma única vez um novo aumento de dificuldade: velocidade +10%, frequência de inimigos/obstáculos +10% e frequência de Sonhos +20%.
- A interpretação adotada para “após 1 minuto” é um único incremento aos 60 segundos do nível 5, sem novos incrementos a cada minuto adicional.

### Versões e validação
- `beta.html` passa para **v0.24**.
- `teste.html` aponta para a beta v0.24.
- `index.html` permanece na versão principal v0.19, sem alterações.
- Validação realizada por inspeção dos trechos alterados e conferência das referências/controles. Ainda é necessário testar visualmente em navegador desktop e celular, principalmente fullscreen, áudio, layout responsivo, persistência do ranking e empate por milissegundos.


## Ajustes — beta v0.25: Sacerdotisa e controles da tela inicial (26/11/2026)

- Removido da tela inicial o texto **“Escolha como deseja começar sua sessão.”**.
- Os botões de **tela cheia** e **música ligada/desligada** foram movidos da tela de tiragem para a tela inicial. O controle de música mantém o estado ligado por padrão e permite ligar/desligar a trilha.
- A Sacerdotisa agora protege automaticamente contra a próxima colisão, tanto com obstáculos quanto com inimigos.
- Ao ativar, inicia a recarga de **15 segundos**. Durante todo esse período, Sonhos não podem ser coletados; a coleta volta a ser permitida quando a recarga termina.
- A descrição da carta foi atualizada para refletir a proteção contra inimigos e obstáculos e o bloqueio temporário de Sonhos.
- Na tela **“Meditação interrompida”**, as explicações dos poderes agora ficam visíveis abaixo de cada carta; a regra CSS que as ocultava foi removida.
- A versão da beta passa para **v0.25**. teste.html aponta para a nova versão. index.html não foi alterada.
- Validação estática: JavaScript analisado sem erros de sintaxe; conferidos os seletores e as condições de colisão, recarga e coleta. Teste visual e de jogabilidade em navegador real ainda pendente.


---

## Atualização de decisões e implementação — 26/11/2026

### Beta v0.26 — sorteio de Sol e Lua

- Removida a restrição que impedia **O Sol** e **A Lua** de aparecerem na mesma tiragem.
- As duas cartas continuam sem repetição e participam do sorteio junto às demais cartas disponíveis.
- Mantida a regra já existente de aumento relativo de 40% no peso da Lua entre 21h e 6h; fora desse período, todas as cartas disponíveis têm o mesmo peso.
- A primeira carta continua seguindo a regra de 90% para A Força.
- beta.html atualizada para v0.26; teste.html aponta para v0.26.
- index.html permanece inalterada.

### Ranking online com Google Sheets e login Google

- Decisão aprovada: o ranking compartilhado usará a planilha Google Sheets indicada pelo usuário e autenticação com conta Google.
- O ranking local atual é provisório e deverá ser substituído pela leitura e gravação remotas.
- A identidade deve ser validada no servidor usando o token de ID do Google; não confiar em nome, e-mail ou identificador enviados isoladamente pelo navegador.
- A planilha será o armazenamento dos resultados. O acesso de gravação deverá passar por um endpoint servidor (por exemplo, Google Apps Script vinculado à planilha), que valide o token e grave os resultados.
- Pendências para concluir a integração:
  - Definir se o login aceitará qualquer conta Google ou somente os cinco jogadores previstos inicialmente.
  - Obter o OAuth Web Client ID do projeto Google Cloud.
  - Criar e publicar o endpoint Apps Script com acesso autorizado à planilha.
  - Confirmar os cabeçalhos/estrutura da aba de ranking e a regra de ordenação/limite.
- A integração não deve ser considerada publicada ou operacional até que as credenciais e o endpoint sejam configurados e testados.

## Decisões atualizadas — autenticação e ranking online (26/11/2026)

Esta seção prevalece sobre qualquer referência anterior a cinco jogadores, ranking fora do escopo, Apps Script ou ausência de contas.

### Acesso e autenticação
- O jogo terá login com Google.
- Somente e-mails cadastrados na aba `jogadoras` da planilha poderão acessar o jogo.
- O limite será de **50 jogadoras cadastradas**.
- O backend será implementado com **Vercel Functions**, usando as credenciais de uma conta de serviço Google para acessar a Google Sheets API.
- O backend deve validar o ID token do Google (assinatura, emissor, audiência, validade e e-mail verificado) e usar o identificador estável `sub` como identidade da conta.
- A autorização será conferida no servidor consultando a aba `jogadoras`; não confiar em e-mail/nome enviados isoladamente pelo navegador.
- A planilha permanece privada e compartilhada com a conta de serviço com permissão de Editor.
- Segredos da conta de serviço ficam somente nas variáveis de ambiente da Vercel. Nunca devem ser versionados no Git.
- O projeto Google Cloud atualmente usado é compartilhado com o aplicativo Contas da Casa por decisão temporária do usuário. Não remover nem alterar o cliente OAuth desse outro aplicativo.

### Registro e classificação
- Cada partida concluída será registrada individualmente na aba `partidas`.
- O ranking exibirá **todas as partidas**, não apenas a melhor ou a última partida de cada jogadora.
- Uma jogadora poderá aparecer várias vezes, uma vez por partida.
- Ordenação: pontuação decrescente; em caso de empate, tempo de jogo decrescente (comparação pelo valor em milissegundos).
- O histórico de partidas não deve ser limitado às 50 melhores; o limite de 50 se refere às jogadoras autorizadas, não ao número de partidas.
- O registro deve incluir, no mínimo, data/hora, identificador Google (`sub`), e-mail autorizado, nome, pontuação, tempo em milissegundos, nível, Sonhos coletados e cartas sorteadas.
- Prever identificador único da partida para evitar duplicidade em reenvios.
- A estrutura real da aba `jogadoras` e seus cabeçalhos ainda precisa ser confirmada antes de implementar leitura e autorização. A aba `partidas` será inspecionada/criada conforme a planilha existente e sem sobrescrever dados.

### Configuração já realizada pelo usuário
- Conta de serviço criada no Google Cloud e chave JSON baixada e guardada localmente.
- Planilha de ranking compartilhada com o e-mail da conta de serviço como Editor.
- Variáveis `GOOGLE_SERVICE_ACCOUNT_EMAIL`, `GOOGLE_PRIVATE_KEY` e `GOOGLE_SHEET_ID` cadastradas na Vercel nos ambientes Production, Preview e Development.
- Cliente OAuth Web criado com o nome `Path of Sanira — Login`.
- `GOOGLE_CLIENT_ID` cadastrado na Vercel nos três ambientes.
- Tela de consentimento configurada como Externo e em teste; e-mail do usuário adicionado como test user; escopos mínimos `openid`, `email` e `profile`.
- Domínios autorizados incluem `pathofsanira.vercel.app` e `c82-casa.vercel.app`; a manutenção conjunta foi aceita temporariamente.
- Ainda não foi realizado deploy nem teste de autenticação/backend.

### Sequência de implementação e publicação
1. Confirmar os cabeçalhos e a estrutura da aba `jogadoras), além da existência/estrutura da aba `partidas`.
2. Implementar e testar endpoints Vercel para autenticação/autorização, leitura de ranking e gravação idempotente de partidas.
3. Integrar o login e o envio/leitura do ranking à `beta.html), incrementando sua versão.
4. Testar contas autorizadas e não autorizadas, persistência, duplicidade, ordenação e funcionamento do jogo.
5. Somente após aprovação explícita do usuário, promover a beta validada para `index.html). Até lá, `index.html` permanece na v0.19.

## Backend inicial — ranking online (26/11/2026)

### Estrutura confirmada da planilha
- Aba de autorização: `jogadoras`.
- Cabeçalhos confirmados: `Email`, `Nome`, `Ativa`.
- Os e-mails são normalizados com remoção de espaços e conversão para minúsculas.
- Somente linhas com `Ativa = TRUE` autorizam login.
- O limite de 50 se aplica ao total de cadastros preenchidos na aba, ativos ou inativos.
- Aba de histórico: `partidas`.
- Cabeçalhos confirmados: `ID_Partida`, `Data_Hora`, `Google_ID`, `Email`, `Nome`, `Pontuacao`, `Tempo_MS`, `Nivel`, `Sonhos`, `Cartas`.

### Arquivos de backend adicionados
- `package.json`: inclui `google-auth-library` para verificar ID tokens Google e autenticar a conta de serviço.
- `api/_lib/google.js`: valida as variáveis de ambiente, verifica ID token (audience/assinatura/validade via biblioteca Google, emissor e e-mail verificado), consulta a aba `jogadoras` e autentica chamadas à Google Sheets API.
- `api/auth.js`: POST para validar login e autorização.
- `api/ranking.js`: GET autenticado para ler todas as partidas, ordenando pontuação decrescente e tempo em milissegundos decrescente.
- `api/partidas.js`: POST autenticado para validar e acrescentar uma partida na planilha; consulta IDs existentes antes de gravar para evitar reenvio duplicado em tentativas comuns.

### Contratos atuais dos endpoints
- `POST /api/auth`: JSON `{ "credential": "<Google ID token>" }`; retorna `{ "user": { "sub", "email", "name" } }` quando autorizado.
- `GET /api/ranking`: cabeçalho `Authorization: Bearer <Google ID token>`; retorna `{ "partidas": [...] }`.
- `POST /api/partidas`: JSON `{ "credential": "<Google ID token>", "partida": { "id", "score", "elapsedMs", "level", "dreams", "cards" } }`.
- A API não recebe nome/e-mail do jogador como fonte de identidade; usa os dados verificados do token e a linha autorizada na planilha.
- O endpoint de partidas faz leitura prévia de IDs antes do append. Isso protege contra retries comuns, mas a consulta e o append não são uma operação atômica; concorrência simultânea excepcional ainda pode duplicar um ID. Avaliar mecanismo de idempotência transacional se necessário.

### Estado e pendências
- Backend inicial versionado na `main`; ainda não houve teste real contra Google Cloud/Sheets nem validação de deploy.
- A interface da beta ainda usa ranking local em `localStorage`; a integração do login e a substituição desse fluxo pelo backend permanecem pendentes.
- Antes de considerar operacional, validar a instalação de dependências na Vercel, configuração das quatro variáveis nos ambientes, acesso da conta de serviço à planilha e os três endpoints.
- A página principal `index.html` continua sem alterações; a beta ainda não foi promovida.

## Integração de login e ranking na beta v0.27 (26/11/2026)

- A versão beta foi incrementada de v0.26 para v0.27.
- A tela inicial apresenta o botão Google Identity Services. O jogo só libera o início após resposta positiva de `POST /api/auth`.
- O Client ID público é obtido por `GET /api/config`, evitando gravar o identificador no HTML.
- Ao finalizar a sessão, a beta envia a partida para `POST /api/partidas` e consulta `GET /api/ranking`; o ranking exibido passa a vir da planilha e inclui todas as partidas.
- O payload da partida usa ID UUID (quando disponível), pontuação, tempo em milissegundos, nível, Sonhos e cores das cartas sorteadas.
- O status de gravação/erro é apresentado na tela final.
- A central `teste.html` aponta para a beta v0.27.
- Arquivo `api/config.js` criado para expor somente o Client ID público ao navegador.
- `index.html` permanece na v0.19, sem alterações.

### Validação pendente antes de considerar v0.27 operacional
- Não foi possível confirmar deploy Vercel nem executar teste no navegador nesta etapa.
- Verificar que o domínio `https://pathofsanira.vercel.app` está cadastrado em Authorized JavaScript origins no cliente OAuth usado.
- Confirmar que `GOOGLE_CLIENT_ID`, `GOOGLE_SERVICE_ACCOUNT_EMAIL`, `GOOGLE_PRIVATE_KEY` e `GOOGLE_SHEET_ID` estão definidos no ambiente de produção da Vercel.
- Testar `GET /api/config`, login com e-mail ativo e bloqueio de e-mail inativo/não cadastrado.
- Testar gravação, consulta do ranking, ordenação e repetição de envio de ID.
- A conta OAuth continua em modo Testing; somente contas adicionadas como test users conseguirão autenticar enquanto permanecer assim.
- A biblioteca `google-auth-library` será instalada pela Vercel a partir do `package.json`; validar build após a instalação.


## Ajuste — beta v0.28: remoção da saudação após login (26/11/2026)

- Removida da tela inicial a frase personalizada exibida após a autorização Google (“Bem-vinda, ...! Você está autorizada.”).
- Após login autorizado, o texto de status fica vazio; o botão Google é ocultado e o botão para iniciar a tiragem é liberado normalmente.
- Mensagem para e-mail não autorizado permanece: **“Este e-mail não está autorizado a acessar o Path of Sanira.”**. A API retorna HTTP 403 e a interface apresenta o texto recebido.
- A central `teste.html` aponta para a beta v0.28.
- A página principal `index.html` permanece inalterada na v0.19.
- Alteração visual ainda depende de conferência no navegador após o deploy.


## Melhoria — cores das cartas no histórico da planilha (26/11/2026)

- A aba `partidas` mantém a coluna `Cartas` com o JSON original das cores hexadecimais.
- Foram acrescentadas as colunas `Carta 1`, `Carta 2` e `Carta 3`, contendo os códigos hexadecimais individuais.
- Ao registrar uma nova partida, o backend aplica a cor de fundo correspondente em cada uma das três células, permitindo visualizar as cartas diretamente na planilha.
- Partidas antigas sem as colunas visuais são migradas automaticamente na próxima gravação de uma nova partida: os códigos são extraídos da coluna `Cartas` e as células recebem a formatação correspondente.
- A mudança está restrita ao backend e à aba `partidas`. A beta permanece na v0.28; `index.html` permanece na versão principal v0.19.
- Os códigos hexadecimais originais são preservados. Se uma cor não estiver em formato hexadecimal válido, seu valor é mantido na coluna original, mas a célula visual correspondente não recebe preenchimento.
- A formatação utiliza a Google Sheets API `spreadsheets.batchUpdate`. O primeiro teste real após o deploy deve confirmar a migração do histórico e a formatação de uma nova partida.


## Melhorias — nomes das cartas, HUD da Torre e catálogo visual (26/11/2026)

- Backend `api/partidas.js`: as colunas `Carta 1`, `Carta 2` e `Carta 3` agora gravam o nome correspondente à cor da carta, mantendo o preenchimento de fundo na cor original. A coluna `Cartas` continua preservando o JSON hexadecimal.
- O backend migra também as linhas históricas: na próxima gravação de uma partida, substitui os códigos hexadecimais das três colunas auxiliares pelos nomes das cartas e reaplica os fundos coloridos.
- O mapeamento atual corresponde às 12 cartas do baralho: O Louco, O Mago, A Sacerdotisa, A Imperatriz, O Carro, A Força, O Eremita, A Roda da Fortuna, A Morte, A Torre, A Lua e O Sol.
- `beta.html` incrementada para v0.29. O botão ⚡ da Torre passa a ficar imediatamente à direita do terceiro nome de carta exibido no HUD, independentemente da posição da Torre na tiragem. Continua condicionado à presença da carta Torre e às regras de uso do poder.
- `Cartas.html` incrementada para v0.6 e reconstruída com as mesmas ilustrações SVG, numeração, cores, nomes e poderes definidos em `beta.html`.
- `teste.html` atualizado para indicar beta v0.29 e catálogo Cartas v0.6.
- `index.html` permanece na v0.19, sem alterações. A beta não foi promovida para a página principal.
- Validar após o deploy: gravação de nova partida, migração dos nomes nas linhas antigas, posição do botão ⚡ em tiragens com Torre em posições diferentes e correspondência visual do catálogo.


## Atualização — beta v0.30 (26/11/2026)

- O título da beta passa para v0.30; `index.html` permanece intocado.
- A credencial Google é mantida em `sessionStorage` para sobreviver a recargas na mesma sessão do navegador. Ao abrir a página, o backend revalida a credencial antes de liberar o jogo; se estiver expirada/inválida, a sessão local é descartada e o Google Identity Services tenta oferecer seleção/autenticação automática (`auto_select`/One Tap), mantendo o botão manual disponível. O ID token não é gravado em `localStorage`.
- O botão Compartilhar gera PNG vertical 1080×1350 com cenário correspondente ao nível final, Sanira renderizada com as cores das cartas, pontuação, posição na classificação online quando disponível e crédito `desenvolvimento por @carlos_h5` no rodapé à direita.
- Em aparelhos/navegadores que suportam compartilhamento de arquivos, usa Web Share API com `File` PNG para abrir a folha nativa do sistema. Em ambientes sem suporte a compartilhamento de arquivos, oferece compartilhamento de texto quando disponível ou salva o PNG.
- Pendente validar em aparelho Android/iOS real a folha nativa e o comportamento de autenticação após expiração do ID token.


## Ajuste — imagem compartilhada da beta v0.31 (26/11/2026)

- Removido da imagem de compartilhamento o texto de situação da partida, incluindo “Meditação interrompida”.
- Removidas as barras/arcos coloridos em volta da personagem.
- As cartas agora aparecem como bolinhas preenchidas com suas cores e os respectivos nomes, seguindo a apresentação compacta do HUD.
- Mantidos cenário do nível final, personagem centralizada, pontuação, posição no ranking e crédito no rodapé à direita.
- `index.html` permanece na v0.19.


## Ajustes — beta v0.32: compartilhamento, transição e ranking (26/11/2026)

- A imagem compartilhada mantém os dados de pontuação e posição do ranking centralizados horizontalmente, independentemente do alinhamento usado na linha das cartas.
- O tempo de transição entre níveis foi reduzido pela metade em todas as fases: preparação de 4 para 2 segundos, dissolução visual de 3 para 1,5 segundo e tela livre após a troca de 5 para 2,5 segundos. A transição completa passa de 12 para 6 segundos.
- O ranking online mantém todas as partidas na lista e passa a ter rolagem vertical com barra visível.
- Ao abrir o ranking, a lista é posicionada para destacar a partida atual no centro, mostrando três posições acima e três abaixo. Se a partida estiver entre as sete primeiras, a lista começa no topo e exibe as sete primeiras.
- O botão **Compartilhar** foi movido para a mesma linha do título **Ranking online**, centralizado horizontalmente no painel.
- beta.html passa para v0.32. index.html permanece na v0.19, sem alterações.
- Validação estática das alterações; conferir visualmente em navegador desktop e celular, especialmente a rolagem, o posicionamento inicial da partida atual e a transição entre níveis.


## Ajuste — beta v0.33: botão compartilhar no ranking e cartas verticais (26/11/2026)

- O botão **Compartilhar** foi retirado do cabeçalho do ranking e inserido somente na linha da partida atual em destaque. Na linha, fica depois da pontuação e imediatamente antes das três bolinhas coloridas das cartas, no espaço entre os dados da partida e as cartas.
- A linha atual do ranking acomoda separadamente posição, nome/nível, pontuação, botão de compartilhamento e bolinhas das cartas. As demais partidas mantêm posição, nome/nível, pontuação e bolinhas.
- Na imagem compartilhada, as três cartas agora são apresentadas verticalmente: uma bolinha colorida e o nome de cada carta em cada linha, uma abaixo da outra. O conjunto fica centralizado horizontalmente.
- O painel de pontuação e classificação foi reposicionado abaixo da lista vertical de cartas para evitar sobreposição.
- beta.html passa para v0.33. index.html permanece na v0.19, sem alterações.
- Validação estática por inspeção do HTML/CSS/JavaScript. Conferir em navegador real o encaixe da linha destacada em telas menores e a imagem PNG gerada.


## Ajuste — beta v0.34: botão Compartilhar ao lado do nível (26/11/2026)

- Na linha da partida atual em destaque no ranking, o botão **Compartilhar** foi movido para dentro da linha de metadados, imediatamente à direita do texto de tempo e nível (por exemplo, “Nível 3”).
- O botão recebeu acabamento visual mais destacado em amarelo, com texto escuro, borda clara e leve realce.
- O botão continua aparecendo somente na partida atual; pontuação e bolinhas das cartas permanecem nas colunas próprias.
- `beta.html` passa para v0.34. `index.html` permanece na v0.19, sem alterações.
- Validar visualmente em telas menores se o botão permanece legível e não comprime o texto do nível.


## Ajuste — beta v0.35: duração da transição e alinhamento do ranking (26/11/2026)

- A transição entre níveis passa a ter três fases: preparação de **3 segundos**, dissolução visual de **2 segundos** e período após a troca de **4 segundos**. A duração total é de **9 segundos**.
- O progresso da dissolução é calculado com a duração real de 2 segundos, para completar a troca visual ao final da fase.
- Na linha da partida atual do ranking, o botão **Compartilhar** fica mais compacto horizontalmente. As três bolinhas das cartas permanecem na mesma linha, sem quebra para uma linha inferior.
- beta.html passa para v0.35. index.html permanece na v0.19, sem alterações.
- Validar visualmente em telas menores o alinhamento da linha atual e a transição entre níveis.


## Correção — beta v0.36: alinhamento das cartas em todas as linhas do ranking (26/11/2026)

- Corrigida a grade CSS geral de `.rank-row`: agora todas as partidas, não apenas a partida atual, reservam quatro colunas para posição, dados da jogadora, pontuação e bolinhas das cartas.
- As três bolinhas permanecem na quarta coluna, na mesma linha da partida. A regra específica da partida atual continua preservando o espaço do botão Compartilhar.
- `beta.html` passa para v0.36. A transição permanece em 3 s + 2 s + 4 s (9 segundos no total). `index.html` continua na v0.19, sem alterações.
- Validação estática do CSS e da estrutura de renderização do ranking; conferir em navegador real em diferentes larguras.


## Compartilhamento — beta v0.37 (26/11/2026)

- A imagem compartilhada agora apresenta **PONTOS** e **TEMPO DE MEDITAÇÃO** lado a lado, em duas colunas equilibradas e separadas por um divisor visual.
- O tempo é exibido no formato **MM:SS**, usando o tempo total decorrido da sessão (elapsedMs).
- A posição no ranking permanece centralizada abaixo das duas métricas.
- O painel mantém o fundo escuro translúcido, com hierarquia visual consistente e leitura organizada.
- A página beta foi atualizada para v0.37. A página principal `index.html` permanece inalterada.


## Tela inicial — beta v0.38: inclusão da arte-base da Sanira (26/11/2026)

- A tela inicial mantém a composição e os controles existentes: título, autenticação/botão de tiragem e controles de tela cheia e música.
- Inserida abaixo do nome a arte-base já existente em `assets/sanira/sanira-frente-modular.svg`, sem criar uma nova ilustração nem alterar o arquivo original da personagem.
- Aplicada somente uma animação CSS discreta de flutuação vertical à imagem na tela inicial.
- Nenhum elemento novo de cenário, moldura, partículas, halo ou botão foi acrescentado. A tela de tiragem e o fluxo de login permanecem inalterados.
- `beta.html` atualizada para v0.38. `index.html` permanece inalterada.
- Validação realizada por inspeção do HTML/CSS e conferência do caminho do SVG existente; teste visual em navegador real ainda pendente.


## Sanira — beta v0.39: faixas e V em cinza escuro (26/11/2026)

- Na arte-base `assets/sanira/sanira-frente-modular.svg`, a variável `--poder` passou de laranja para cinza escuro `#4A4A52`.
- A alteração afeta somente as faixas das mangas e o V do peito, que compartilham essa variável no SVG. A silhueta, demais cores, formas e animação da tela inicial permanecem inalteradas.
- `beta.html` atualizada para v0.39. `index.html` permanece inalterada.


## Interpretação combinada do Tarot — beta v0.40 (26/11/2026)

- Criado `data/interpretacoes-tarot.json`, com as 12 cartas do baralho, 220 combinações de três cartas sem distinção de ordem e três mensagens por combinação (660 textos no total).
- As mensagens foram redigidas para o jogo em tom intermediário e reflexivo, sem tratar os resultados como previsões inevitáveis. A estrutura do banco mantém os textos separados do código da interface.
- Ao terminar as vidas, a partida continua sendo registrada no backend e o jogo abre a modal **“Interpretação da sua tiragem”**, com as três bolinhas nas cores reais das cartas e uma das três mensagens escolhida aleatoriamente.
- O botão **Continuar** leva ao ranking online já existente. A lista, o destaque da partida e o compartilhamento permanecem no fluxo atual.
- A chave da combinação é formada pelos IDs das cartas em ordem alfabética, garantindo que a mesma trinca encontre o mesmo registro independentemente da ordem sorteada.
- `beta.html` passa para v0.40. `index.html` permanece inalterada.
- Fontes consultadas como referência conceitual: Personare (narrativa integrada em tiragens de três cartas), Learn Tarot/Joan Bunning (leitura como história), Biddy Tarot e Clube do Tarô. Os textos do JSON são originais, não transcrições dessas fontes.
- Validação estática da integração; testar no navegador o carregamento do JSON, a escolha da mensagem, a modal e o avanço ao ranking.
