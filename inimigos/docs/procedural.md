# Jogos procedurais: notas para o Path of Sanira

**Atenção:** esta conversa explicou o conceito e levantou ideias. **Nada aqui foi decidido ainda.** Os itens da última seção são perguntas abertas.

## O que é

Jogo procedural é aquele em que parte do conteúdo (fases, terreno, inimigos, itens) é gerada por regras e sorteios enquanto se joga, em vez de ser desenhada à mão e igual para todos.

- **Regras mais sorte:** o sorteio acontece dentro de regras. Exemplo: "um obstáculo a cada 250 a 400 pixels, sem dois tipos difíceis seguidos".
- **Semente (seed):** número que alimenta o gerador. Com a mesma semente, o resultado é sempre igual. Serve para "desafio do dia" e para repetir uma corrida.

## Técnicas comuns

- **Ruído suave (Perlin ou simplex):** curvas naturais, como as colinas e ladeiras de Alto's Adventure.
- **Pedaços prontos (chunks):** trechos curtos desenhados à mão, encaixados em ordem aleatória. É o mais usado em runners.
- **Pesos de sorteio:** como a Força, que sai em 90% das vezes como 1ª carta.
- **Curva de dificuldade:** velocidade e frequência dos inimigos aumentam com a distância.

## Cuidados

- **Justiça:** o gerador não pode criar algo impossível, como um obstáculo maior do que o pulo alcança.
- **Repetição:** aleatório demais, sem variedade, enjoa. As versões alternativas dos inimigos ajudam.
- **Teste:** simular muitas corridas para achar combinações injustas.

## O que já existe no jogo

- A tiragem das 3 cartas, com peso de 90% para a Força.
- As moedas douradas sorteadas (2 entre 10, ou 4 com a Roda da Fortuna).
- A posição dos obstáculos na demo, que é fixa e não gerada.

## Ideias a decidir (nada decidido)

1. O terreno da ladeira será gerado por ruído ou montado com trechos prontos por mundo?
2. Os inimigos serão escolhidos por peso conforme o mundo (por exemplo, versões Pântano na floresta, Gelo na neve e Magma no vulcão)?
3. Haverá semente e "desafio do dia"?
4. Quais regras de justiça valem (distância mínima entre obstáculos, altura máxima em relação ao pulo)?
5. Como cresce a dificuldade com a distância?
6. Como o resultado das cartas afeta a geração (por exemplo, a Lua e a Torre mudando os trechos)?
