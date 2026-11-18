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
|-------|----------------|
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
- [ ] Desenhar a aura da Força com a silhueta de focinho de leão na frente (lado direito), no mesmo tom de laranja (pedido feito em 17/11/2026, ainda não desenhado).
- [ ] Decidir se o design `Cartas-Tarot.html` e os SVGs de `assets/cartas/tarot/` substituem o catálogo `Cartas.html` e a arte das cartas no jogo.
- [ ] Decidir quais versões alternativas dos inimigos entram em cada mundo.
- [ ] Responder às perguntas em aberto da seção “Telas procedurais: como funcionam e como aplicar”.

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
|-------|------------------------|
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

```
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

- Geração procedural de obstáculos e dificuldade crescente (ver a seção “Telas procedurais: como funcionam e como aplicar”).
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
|-------|-------------------------|
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

## Cartas tarot e inimigos com versões alternativas — 17/11/2026

Esta atualização trata de arte e componentes isolados. Nada aqui foi integrado ao jogo (`beta.html`, `v0.5.html` e `index.html` permanecem inalterados). A integração depende de solicitação explícita, conforme a política de versões.

### Design de cartas no estilo tarot monocromático

- **Arquivos novos:**
  - `Cartas-Tarot.html` (v0.1): grid 3x4 com as 12 cartas.
  - `Cartas-Minimalista.html` (v0.1): versão alternativa, com um símbolo simples de uma cor por carta.
  - `assets/cartas/tarot/carta-NN-nome.svg`: os 12 desenhos soltos (por exemplo `carta-08-a-forca.svg`), cada um na cor do poder, com 100 x 120 de área.
- **Design em uso:** o tarot monocromático, aprovado pelo usuário após ajustes. A versão minimalista fica como alternativa e não substitui o catálogo atual.
- **Regras do design:**
  - Fundo da carta na cor atual (`#1B1740`), igual em todas.
  - Todo o resto (moldura, desenho, número, nome e textos) usa a cor do poder da carta (seção 9), em camadas de opacidade: 100%, 55% e 25% da cor sobre o fundo, mais as partes escuras na cor do fundo.
  - Desenhos inspirados nas cenas clássicas do tarot, em formas planas e simples.
  - Layout: número romano no alto, desenho em moldura, nome em fonte clássica (Cinzel) e, abaixo, poder e descrição (Inter). A Força mantém a etiqueta “1ª · 90%”.
- **Ajustes aprovados nos desenhos:**
  - A Força: apenas o círculo do leão (juba, rosto, olhos, nariz e boca), grande e centralizado.
  - O Mago: sem o símbolo de infinito.
  - O Sol: sem rosto.
  - O Carro: sem a figura humana, apenas o carro.
- **Referências publicadas (designs):**
  - Tarot monocromático: https://claude.ai/artifact/HVRjgwq1PxWUfhT6Gg64wb
  - Minimalista: https://claude.ai/artifact/6EYrUZ5XTR8HxMEcBfE171
- **Textos das cartas:** seguem o catálogo de poderes anterior (por exemplo, O Carro ainda cita o dash na descrição do design). Antes de integrar, sincronizar com a regra consolidada (seção 5 das decisões).

### Inimigos — `Inimigos.html` v0.2

- Mantidas as funções `drawAlligator`, `drawCattle`, `drawToucan` e `drawEnemy`, todas com `(x, y, w, h)` (`y` é a base). Todas ganharam um último parâmetro **opcional** com o tema visual; sem ele, usam o padrão. **Largura e altura de cada inimigo não mudaram**, então a colisão é a mesma.
- Tamanhos: jacaré 76 x 38, gado 62 x 68, tucano 52 x 42 e inimigo genérico 44 x 50.
- Desenhos refeitos em formas planas e cores suaves (versão v0.1) e agora com **três alternativas** por inimigo, trocando cores e texturas:

| Inimigo | Padrão | Alternativa 1 | Alternativa 2 | Alternativa 3 | Cartas |
|---------|--------|---------------|---------------|---------------|--------|
| Jacaré | Verde | Pântano (verde-oliva, manchas) | Albino (creme, escamas) | Gelo (azul, cristais) | Verde `#6CC38A` |
| Gado | Creme com manchas | Marrom com manchas brancas | Preto com chifres claros | Peludo laranja com pelos | Laranja `#F28C28` |
| Tucano | Preto com bico amarelo | Azul com bico vermelho | Escarlate com bico claro | Albino com penas | Ciano `#5FCFE0` |
| Genérico | Roxo | Limo (verde, bolhas) | Magma (vermelho, rachaduras) | Gelo (azul, facetas) | Roxo `#A78BDB` |

- **Versão “Cartas”:** monocromática sobre o fundo escuro das cartas, com tons de uma só cor por inimigo (as cores da última coluna acima, escolhidas entre as cores dos poderes). Quando selecionada, o cenário também escurece.
- A página tem um seletor “Estilo” (padrão, três alternativas e cartas) para o cenário e a ampliação, e uma **galeria** com as 5 versões dos 4 inimigos.
- **Sugestão de uso por mundo (a decidir, ver pontos em aberto):** Pântano na floresta, Gelo na neve e Magma no vulcão. Fábricas, espaço e outra dimensão ainda não têm versões.
- O tucano bate as asas usando o relógio do navegador (`performance.now()`), sem estado extra.

## Telas procedurais: como funcionam e como aplicar

> **Como ler esta seção.** O que está marcado como **Decidido** vem de decisões do usuário registradas neste documento. O que está marcado como **Proposta** é uma sugestão técnica para o projeto e **ainda não foi decidida**. O que está marcado como **Em aberto** precisa de decisão antes de implementar. Nada aqui foi integrado ao jogo.

Neste jogo, uma **tela procedural** é cada trecho do percurso que aparece à frente de Sanira, gerado por regras e sorteio em vez de ser fixo. O jogador percorre um trecho novo a cada corrida, mas dentro de limites que garantem que ele seja justo e possível.

### 1. Status das decisões

| Tema | Estado | Fonte |
|------|--------|-------|
| Na versão final o percurso é procedural e diferente a cada corrida | **Decidido** | Decisões consolidadas, item 1 |
| A corrida final é infinita; nos testes, a corrida segue limitada | **Decidido** | Decisões consolidadas, item 1 |
| Nos testes, manter uma quantidade razoável de elementos, parecida com a atual | **Decidido** | Decisões consolidadas, item 1 |
| Sonhos com distribuição procedural na versão final | **Decidido** | Decisões consolidadas, item 3 |
| Dificuldade: mais obstáculos e mais velocidade; a velocidade só cresce a partir do nível 3 | **Decidido** | Decisões consolidadas, item 1 |
| Sequência de sete mundos | **Decidido** | Decisões consolidadas, item 7 |
| Hoje: tipo e posição dos elementos são sorteados a cada sessão, em quantidade limitada | **Existe na V2 v0.4 e nas páginas derivadas** | Seção 13 |
| Critérios dos níveis, teto de velocidade, relação mundos x níveis | **Em aberto** | Lembretes e pendências |
| Buracos e armadilhas | **Em aberto** (removidos temporariamente) | Seção 13 |
| Arquitetura, trechos, regras de justiça, terreno por ruído e semente | **Proposta** | Esta seção |

### 2. Como funciona

Um gerador procedural junta quatro peças:

1. **Semente (seed):** um número que alimenta o sorteio. A mesma semente gera sempre o mesmo percurso. Permite repetir uma corrida e investigar falhas.
2. **Trechos (chunks):** pedaços de percurso, com comprimento fixo e uma lista de elementos (obstáculos, inimigos, Sonhos) em posições relativas ao início do trecho.
3. **Regras:** dizem quais trechos podem vir depois de quais, com que peso, e o que é proibido.
4. **Validação de justiça:** confere que o percurso gerado é possível mesmo no pior caso (sem nenhum poder).

O fluxo, a cada corrida:

```
semente → gerador escolhe trechos (pesos por mundo e nível) → posiciona elementos
        → valida justiça → o jogo desenha só o que está à frente da câmera
```

O gerador trabalha **à frente** da câmera: enquanto o último trecho gerado estiver a menos de duas telas de distância, sorteia o próximo. Trechos já passados são descartados, para a corrida infinita não consumir memória.

### 3. Peças da proposta técnica

#### 3.1 Semente e gerador de números aleatórios — **Proposta**

Trocar `Math.random()` por um gerador com semente, como o mulberry32:

```js
function criarAleatorio(semente) {
  return function () {
    semente |= 0; semente = (semente + 0x6D2B79F5) | 0;
    let t = Math.imul(semente ^ (semente >>> 15), 1 | semente);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
```

- Usar **geradores separados** para sistemas diferentes: um para o percurso, outro para a tiragem das cartas e outro para efeitos visuais. Assim, uma carta sorteada não muda o percurso da mesma semente.
- Exibir a semente na tela final facilita reproduzir um problema relatado.

#### 3.2 Formato dos trechos — **Proposta**

```json
{
  "id": "pedras-pares",
  "mundos": ["planicie", "floresta"],
  "dificuldade": 1,
  "comprimento": 700,
  "elementos": [
    { "tipo": "pedra",  "x": 200 },
    { "tipo": "pedra",  "x": 330 },
    { "tipo": "sonho",  "x": 520, "altura": "ar" },
    { "tipo": "tucano", "x": 640, "altura": "alta" }
  ]
}
```

- `mundos` diz em quais ambientes o trecho pode aparecer; `dificuldade` o liga aos níveis; `x` é a posição dentro do trecho.
- Há dois jeitos de criar trechos: **escritos à mão** (controle total do desenho) ou **montados por regras** a partir de peças (mais variedade). A proposta é começar com trechos à mão e adicionar montagem por regras depois.

#### 3.3 Regras de justiça — **Proposta**

O gerador deve garantir que o percurso é possível **sem nenhum poder**, porque as cartas mudam de corrida para corrida.

1. **Distância mínima entre obstáculos consecutivos:** velocidade × (tempo de voo do pulo + tempo de reação). Com os valores da demo (gravidade 1800 px/s², pico do pulo 70 px, velocidade 300 px/s), o tempo de voo é cerca de 0,56 s e a distância mínima fica em torno de 270 px com 0,35 s de reação. Recalcular quando a velocidade aumentar, porque a distância precisa crescer junto.
2. **Altura máxima:** nenhum obstáculo pode ser mais alto do que o pico do pulo básico menos uma margem (por exemplo, 80% do pico). Calibrar com a colisão real.
3. **Sequências difíceis:** no máximo N elementos difíceis seguidos, seguidos de um trecho de respiro (só Sonhos, sem obstáculos).
4. **Sonhos:** nunca dentro de obstáculos; ficam em arcos alcançáveis pelo pulo básico, com alguns mais altos como recompensa.
5. **Inimigos móveis:** o jacaré (horizontal) e o tucano (voador) precisam de espaço extra e não podem sobrepor outros obstáculos no mesmo ponto.
6. **Poderes que interferem:** a Lua reduz a visibilidade, então trechos muito densos com a Lua devem ter mais respiro; a Torre limpa a tela e a Sacerdotisa atravessa obstáculos (não inimigos). O gerador **não pode depender** desses poderes para ser possível.

#### 3.4 Dificuldade por nível — **Proposta com base em decisões**

- Decidido: a dificuldade aumenta a frequência de obstáculos e a velocidade; a velocidade só começa a crescer no **nível 3**, com um teto.
- Proposta de forma:
  - O nível sobe com a distância percorrida (critérios em aberto).
  - Cada nível altera os **pesos** dos trechos (mais trechos difíceis em níveis altos) e a densidade dos elementos.
  - A velocidade: `v = min(vMax, v0 × (1 + k × (nível − 2)))` para nível ≥ 3, e `v0` antes disso. Os valores de `k` e `vMax` estão em aberto.

#### 3.5 Mundos — **Proposta com base em decisões**

- Decidido: sete ambientes, em ordem (planície, floresta, neve, fábricas, vulcão, espaço e outra dimensão); transição e duração em aberto.
- Proposta: cada mundo é um conjunto de dados com paleta de cores, trechos permitidos, inimigos que aparecem (e suas versões alternativas) e regras de terreno.
- Sugestão de uso das versões alternativas dos inimigos (**a decidir**): Pântano na floresta, Gelo na neve e Magma no vulcão. Para fábricas, espaço e outra dimensão ainda não existem versões.

#### 3.6 Terreno — **Proposta**

- Decidido: Sanira acompanha a inclinação da ladeira.
- Proposta: gerar a ladeira como uma curva suave (por exemplo, ruído unidimensional ou soma de senos) com **limites de inclinação** mínima e máxima, para que o jogo continue legível e justo. Os obstáculos usam a altura do terreno na posição `x`, como já acontece nas versões atuais.

### 4. Como aplicar no projeto — passos propostos

Seguindo a política de versões, cada etapa deve gerar uma nova versão e commits separados por página. Sugestão de etapas:

1. **Semente e gerador com semente** na beta, sem mudar a jogabilidade. Mostrar a semente na tela final.
2. **Percurso atual como lista de trechos** em formato de dados (JSON), com o jogo consumindo essa lista.
3. **Gerador por pesos** dentro dos limites atuais de teste (quantidade razoável de elementos), com as regras de justiça da seção 3.3.
4. **Componente isolado de teste do percurso** na central, por exemplo `Percurso.html` (nome sugerido), v0.0: mostra a linha do tempo de trechos, botão “nova semente” e relatório das regras de justiça.
5. **Bot de teste:** simular milhares de sementes sem poderes e verificar que todo percurso é possível; listar as sementes que falham.
6. **Níveis e limite de velocidade** (depende das decisões em aberto), depois a **corrida infinita**.
7. **Mundos e versões alternativas dos inimigos.**
8. **Terreno por ruído.**
9. Opcional: **semente do dia** (todos os cinco jogadores correm o mesmo percurso, o que facilita comparar resultados) ligada ao registro em Google Sheets, se essa integração for decidida.

### 5. Cuidados

- **Aleatório demais cansa:** variar sempre dentro de regras e usar as versões alternativas dos inimigos para manter a corrida interessante.
- **Reprodutibilidade:** guardar a semente de cada corrida; usar geradores separados por sistema (percurso, cartas, efeitos).
- **Desempenho:** gerar à frente da câmera e descartar o que ficou para trás; não recalcular o percurso a cada quadro.
- **Teste automatizado:** cada alteração nas regras deve passar pelo bot de simulação antes de ir para o jogo.
- **Separar ajuste de dificuldade de geração:** o gerador cria percursos possíveis; os níveis só mudam pesos e velocidade.

### 6. Perguntas em aberto

1. O terreno será gerado por ruído ou montado com trechos prontos por mundo?
2. Os trechos serão escritos à mão, montados por regras ou os dois?
3. Quais são os critérios dos níveis (distância, tempo ou pontuação) e o valor do limite de velocidade?
4. Quais versões dos inimigos entram em cada mundo?
5. Haverá semente do dia e ela se liga ao registro dos cinco jogadores?
6. Buracos e armadilhas voltam ao percurso? Se sim, como o gerador os trata?
7. Quais valores de justiça valem (distância mínima, altura máxima, tamanho máximo de uma sequência difícil)?
8. Como as cartas afetam a geração, se afetarem (por exemplo, a Lua e a Torre)?

## Registro de atualizações deste documento — 17/11/2026

- Mantido todo o conteúdo anterior, sem alterações nas decisões.
- Adicionados:
  - Pendências novas em “Lembretes e pendências para decisões futuras” (aura da Força com focinho de leão, uso do design tarot, versões de inimigos por mundo e perguntas de telas procedurais).
  - Referência à seção de telas procedurais na Fase 2.
  - Seção “Cartas tarot e inimigos com versões alternativas — 17/11/2026”.
  - Seção “Telas procedurais: como funcionam e como aplicar”.
