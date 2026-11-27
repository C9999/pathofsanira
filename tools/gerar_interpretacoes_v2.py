#!/usr/bin/env python3
"""Gera data/interpretacoes-tarot.json (v2.0).

Mantém as 12 cartas, as 220 chaves (ordem canônica) e as 3 mensagens por
combinação. Cada mensagem é montada a partir de textos escritos à mão para
cada PAR de cartas (66 pares): como o par é o mesmo em qualquer ordem de
sorteio, a leitura não depende da ordem em que as cartas aparecem.
Uso: python3 tools/gerar_interpretacoes_v2.py data/interpretacoes-tarot.json
"""
import json, sys, itertools

IDS = ["louco","mago","sacer","imper","carro","forca","eremita","roda","morte","torre","lua","sol"]

# risco (sombra) de cada carta, usado depois de "alerta para o risco de ..."
RISCO = {
 "louco":"agir sem pensar nas consequências",
 "mago":"prometer mais do que se entrega, usando o talento só para convencer",
 "sacer":"guardar demais para si e deixar de dizer o que se percebe",
 "imper":"cuidar de tudo e de todos e esquecer de si",
 "carro":"avançar à força, sem ouvir o que está ao redor",
 "forca":"confundir autocontrole com reprimir o que se sente",
 "eremita":"se isolar além do necessário",
 "roda":"esperar que a sorte resolva o que pede uma escolha",
 "morte":"adiar um fim que, por dentro, já aconteceu",
 "torre":"resistir ao que já está desabando",
 "lua":"tomar o medo ou a fantasia por fatos",
 "sol":"enxergar só o lado bom e ignorar o que pede cuidado",
}

# (s = o que acontece quando as duas se encontram; c = conselho)
PAR = {
("louco","mago"):("o impulso de começar encontra a habilidade de executar, e a ideia ganha mãos","Escolha uma primeira ação pequena e concreta antes de planejar o resto"),
("louco","sacer"):("a vontade de saltar esbarra na voz que pede silêncio, e a pressa conversa com a intuição","Escute o que você já sabe por dentro antes de dar o próximo passo"),
("louco","imper"):("a leveza do recomeço encontra a generosidade de quem cuida, e algo novo pode crescer sem pressão","Deixe o novo crescer no seu tempo, com cuidado e sem exigir resultado imediato"),
("louco","carro"):("a espontaneidade ganha um rumo, mas o entusiasmo pode correr mais do que o mapa","Defina para onde quer ir, mas deixe espaço para mudar de caminho"),
("louco","forca"):("a coragem de começar encontra a firmeza de se manter, e o medo vira aliado em vez de freio","Dê o passo com confiança e trate o próprio medo com gentileza, sem brigar com ele"),
("louco","eremita"):("a vontade de ir em frente conversa com a necessidade de parar, e um começo pode nascer da pausa","Reserve um tempo a sós para saber se o impulso é desejo ou fuga"),
("louco","roda"):("o salto se encontra com os ciclos da vida, e uma virada pode abrir portas inesperadas","Fique atento às oportunidades que surgem sem aviso e aceite que nem tudo se controla"),
("louco","morte"):("um fim abre espaço para um começo, e deixar para trás o que pesava libera o caminho","Encerre com consciência o que já cumpriu seu papel para poder recomeçar mais leve"),
("louco","torre"):("uma sacudida pode forçar um novo começo, e o que ruiu deixa terreno livre","Em vez de reconstruir o antigo, pergunte o que você quer experimentar agora"),
("louco","lua"):("o entusiasmo avança por um terreno ainda nebuloso, e a confiança convive com a dúvida","Avance com cuidado e confira o que é intuição e o que é medo antes de decidir"),
("louco","sol"):("o começo vem com clareza e alegria, e a confiança ganha luz","Aproveite o ânimo para experimentar, mostrar o que está nascendo e se divertir no processo"),
("mago","sacer"):("a ação consciente encontra o saber silencioso, e o que se faz passa a refletir o que se sente","Alinhe o que você quer fazer com o que sente que é verdadeiro"),
("mago","imper"):("o talento encontra um terreno fértil, e a ideia pode render quando recebe tempo e cuidado","Invista energia no que você quer ver crescer e cuide do projeto com constância"),
("mago","carro"):("recursos e vontade se somam, e o plano ganha direção e velocidade","Concentre as ferramentas que você tem em um único objetivo e comece a avançar"),
("mago","forca"):("a habilidade encontra o autocontrole, e o poder de agir passa a ser usado com delicadeza","Use sua capacidade com paciência, sem forçar os resultados"),
("mago","eremita"):("o fazer encontra o estudar, e o talento se aprofunda quando passa pela reflexão","Dedique tempo a aprender e a refinar antes de mostrar o resultado"),
("mago","roda"):("a iniciativa encontra a maré dos acontecimentos, e agir na hora certa faz toda a diferença","Observe o momento e aja quando a oportunidade se abrir, sem esperar a condição perfeita"),
("mago","morte"):("a capacidade de criar encontra a necessidade de soltar, e transformar exige abandonar uma forma antiga","Escolha o que precisa ser deixado para que o novo possa ser feito"),
("mago","torre"):("um plano esbarra em um imprevisto, e a ruptura mostra o que estava mal sustentado","Reveja as bases do que você está construindo e reforce o que ficou frágil"),
("mago","lua"):("a clareza de intenção convive com uma névoa de dúvidas, e nem tudo o que se mostra é o que parece","Cheque os fatos antes de agir e desconfie de promessas bonitas demais"),
("mago","sol"):("o talento aparece com confiança, e o que você faz ganha visibilidade e reconhecimento","Mostre o seu trabalho com naturalidade e divida o que sabe"),
("sacer","imper"):("o silêncio interior encontra o acolhimento, e o que se sente ganha espaço para amadurecer","Cuide do que está em gestação sem exigir que se revele antes da hora"),
("sacer","carro"):("a quietude encontra o movimento, e avançar com sabedoria pede ouvir antes de acelerar","Pare um instante para confirmar o rumo antes de pisar no acelerador"),
("sacer","forca"):("a intuição e a coragem serena caminham juntas, e a calma passa a ser uma forma de poder","Confie no seu ritmo e na sua percepção, sem precisar provar nada a ninguém"),
("sacer","eremita"):("dois recolhimentos se encontram, e a busca por respostas vai para dentro","Aceite um período de silêncio e de estudo e evite se cobrar respostas rápidas"),
("sacer","roda"):("o que está oculto encontra os ciclos do destino, e certas coisas se revelam quando chega a hora","Observe os sinais e respeite o tempo de amadurecimento das situações"),
("sacer","morte"):("a intuição pressente um fim, e perceber o que acabou já é metade da transformação","Reconheça o que você já sabe que terminou e permita-se sentir isso"),
("sacer","torre"):("o que estava guardado vem à tona de repente, e uma verdade escondida pode derrubar uma certeza","Receba a revelação com honestidade, sem negar o que ela mostra"),
("sacer","lua"):("a intuição se aprofunda em águas misteriosas, e sonhos, pressentimentos e dúvidas se misturam","Anote o que você sente e dê tempo para que o significado fique claro"),
("sacer","sol"):("o que estava em segredo é iluminado, e a intuição ganha clareza","Confie no que ficou evidente e fale com franqueza sobre o que você percebe"),
("imper","carro"):("o cuidado encontra a direção, e conquistar algo pode caminhar junto com preservar o que importa","Avance sem abandonar o que você ama e o que pede atenção no caminho"),
("imper","forca"):("o acolhimento encontra a coragem serena, e a gentileza se mostra mais forte do que a dureza","Resolva o que for difícil com paciência e afeto, sem agressividade"),
("imper","eremita"):("o cuidado se volta para dentro, e a solidão pode ser um modo de se nutrir","Reserve um espaço de descanso para si antes de se doar de novo"),
("imper","roda"):("a abundância encontra os ciclos, e o que foi semeado pode render quando a estação muda","Aceite o tempo da colheita e continue cuidando do que plantou"),
("imper","morte"):("o que cresceu encontra o fim de uma etapa, e deixar ir também é uma forma de cuidar","Honre o que foi vivido e abra espaço para uma nova fase"),
("imper","torre"):("um lar, um vínculo ou um projeto de que você cuida é sacudido, e o que parecia seguro pede revisão","Proteja o essencial e aceite refazer o que não resistiu"),
("imper","lua"):("o afeto encontra emoções profundas, e a sensibilidade pode ficar à flor da pele","Acolha o que sente sem tomar decisões definitivas no calor da emoção"),
("imper","sol"):("o carinho encontra a alegria, e relações e projetos tendem a florescer","Celebre o que vai bem e compartilhe essa abundância com quem está por perto"),
("carro","forca"):("a vontade de vencer encontra a coragem tranquila, e o controle pode vir pela firmeza em vez da força bruta","Mantenha o foco com paciência, guiando as situações sem atropelar"),
("carro","eremita"):("a pressa encontra a pausa, e avançar bem exige parar para conferir o caminho","Desacelere o suficiente para rever o rumo antes da próxima etapa"),
("carro","roda"):("o esforço pessoal encontra o movimento do destino, e parte do caminho depende do que não se controla","Faça a sua parte e deixe espaço para o que não depende de você"),
("carro","morte"):("o avanço encontra um corte, e seguir adiante pode exigir abandonar o veículo antigo","Troque de rota ou de método se o atual já não leva a lugar nenhum"),
("carro","torre"):("o rumo traçado é interrompido, e um imprevisto obriga a recalcular","Pare, avalie os danos e retome a direção sem se culpar"),
("carro","lua"):("a determinação avança por uma estrada com pouca visibilidade, e a velocidade pede cuidado","Reduza a marcha até enxergar com mais clareza o que há à frente"),
("carro","sol"):("o esforço encontra um bom resultado, e a vitória tende a vir acompanhada de alegria","Siga com confiança e reconheça o seu mérito sem esquecer de quem ajudou"),
("forca","eremita"):("a coragem serena encontra a sabedoria solitária, e a força interior ganha profundidade","Use o silêncio para fortalecer sua confiança, sem se isolar além do necessário"),
("forca","roda"):("a firmeza interior encontra um tempo de mudanças, e a calma ajuda a atravessar as viradas","Mantenha o seu centro quando tudo se movimenta e confie na sua resistência"),
("forca","morte"):("a coragem encontra o fim de um ciclo, e atravessar a perda com serenidade é um ato de força","Permita-se sentir e siga com paciência e compaixão por si mesmo"),
("forca","torre"):("a firmeza é testada por uma ruptura, e a resiliência aparece quando a estrutura cai","Respire e reconstrua com calma, sabendo que você é maior do que o abalo"),
("forca","lua"):("a coragem encontra os medos e as sombras, e domar o que assusta passa pela gentileza","Olhe para o seu receio com compaixão, em vez de lutar contra ele"),
("forca","sol"):("a confiança serena encontra a alegria, e a vitalidade pode se expressar sem esforço","Siga no seu ritmo e deixe a autoconfiança aparecer de forma natural"),
("eremita","roda"):("a busca interior encontra o fluxo da vida, e uma pausa pode revelar o sentido de um ciclo","Use o recolhimento para entender o que o ciclo atual está ensinando"),
("eremita","morte"):("o recolhimento encontra um encerramento, e o luto pode pedir tempo e silêncio","Dê a si mesmo o tempo necessário para elaborar o que terminou"),
("eremita","torre"):("a reflexão encontra uma ruptura, e a solidão pode vir como consequência de uma verdade que veio à tona","Procure a sua luz própria quando as certezas caem e aceite ajuda de quem merece confiança"),
("eremita","lua"):("a busca interior atravessa um terreno incerto, e a lamparina ilumina apenas o próximo passo","Caminhe um passo de cada vez, sem exigir de si a visão do trajeto inteiro"),
("eremita","sol"):("a sabedoria conquistada no silêncio encontra a clareza, e a luz própria pode enfim ser compartilhada","Divida com os outros o que você aprendeu no seu tempo a sós"),
("roda","morte"):("o ciclo vira e um fim se mostra necessário, e a mudança faz parte do movimento natural da vida","Acompanhe a virada em vez de resistir a ela"),
("roda","torre"):("o destino sacode a estrutura, e viradas bruscas podem reorganizar o cenário","Mantenha a flexibilidade e adapte-se ao que mudou"),
("roda","lua"):("os ciclos passam por uma fase de incerteza, e o que vem a seguir ainda não está claro","Espere antes de concluir e observe como as coisas se desenvolvem"),
("roda","sol"):("a virada traz boa fortuna, e um ciclo favorável pode se abrir","Aproveite a boa fase com gratidão, lembrando que ela também faz parte de um ciclo"),
("morte","torre"):("um fim e uma ruptura se encontram, e a mudança pode vir de forma intensa e difícil de evitar","Aceite que algo precisa acabar e cuide de si enquanto a poeira baixa"),
("morte","lua"):("o encerramento encontra o território da incerteza, e o luto vem misturado a dúvidas e sonhos","Dê nome ao que você sente antes de decidir e acolha a confusão sem pressa"),
("morte","sol"):("o fim abre caminho para a luz, e a transformação tende a trazer alívio e clareza","Confie que o que ficou para trás abriu espaço para algo mais vivo"),
("torre","lua"):("a ruptura deixa o terreno nebuloso, e as certezas desabam enquanto as dúvidas crescem","Cuide da sua base emocional e evite decisões drásticas enquanto a névoa não baixa"),
("torre","sol"):("depois do abalo vem a clareza, e o que caiu abre espaço para um recomeço mais honesto","Reconstrua com transparência, usando o que o abalo ensinou"),
("lua","sol"):("a dúvida encontra a luz, e a névoa pode ceder à medida que as coisas se mostram","Esclareça o que ficou obscuro e deixe a verdade aparecer devagar"),
}

def par(a, b):
    i = IDS.index
    return PAR[(a, b) if i(a) < i(b) else (b, a)]

def mensagens(a, b, c, N):
    sab, cab = par(a, b); sbc, cbc = par(b, c); sac, cac = par(a, c)
    return [
        f"Entre {N[a]} e {N[b]}, {sab}. {N[c]} amplia a leitura: entre {N[b]} e {N[c]}, {sbc}. {cac}. {N[c]} também alerta para o risco de {RISCO[c]}.",
        f"Olhe primeiro para {N[b]} e {N[c]}: {sbc}. Quando {N[a]} entra na leitura, entre {N[a]} e {N[c]}, {sac}. {cab}. {N[a]} pede atenção ao risco de {RISCO[a]}.",
        f"Entre {N[a]} e {N[c]}, {sac}. {N[b]} completa o triângulo: entre {N[a]} e {N[b]}, {sab}. {cbc}. {N[b]} lembra o risco de {RISCO[b]}.",
    ]

def main(saida):
    cartas = {"louco":"O Louco","mago":"O Mago","sacer":"A Sacerdotisa","imper":"A Imperatriz","carro":"O Carro","forca":"A Força","eremita":"O Eremita","roda":"A Roda da Fortuna","morte":"A Morte","torre":"A Torre","lua":"A Lua","sol":"O Sol"}
    comb = {}
    for a, b, c in itertools.combinations(IDS, 3):
        comb[f"{a}_{b}_{c}"] = {"cartas": [a, b, c], "mensagens": mensagens(a, b, c, cartas)}
    out = {"versao":"2.0","titulo":"Interpretação da sua tiragem",
           "criterio":"Combinações sem distinção de ordem; três mensagens por combinação, escritas a partir do significado de cada par de cartas.",
           "cartas":cartas,"combinacoes":comb}
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(len(comb), "combinações,", sum(len(v["mensagens"]) for v in comb.values()), "mensagens")

if __name__ == "__main__":
    assert len(PAR) == 66, len(PAR)
    main(sys.argv[1] if len(sys.argv) > 1 else "data/interpretacoes-tarot.json")