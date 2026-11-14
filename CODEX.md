# Path of Sanira — Escopo e fases

## 1. Visão geral

Endless run para o navegador do celular, no estilo de Alto's Adventure: cenário fluido, ritmo calmo, controle por toques na tela.

No início de cada corrida é feita uma tiragem de tarot: 3 cartas são sorteadas e cada uma dá um poder à personagem, no estilo dos upgrades de Mega Man X. No fim da corrida, o jogo mostra uma frase baseada nas cartas sorteadas e na pontuação.

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

