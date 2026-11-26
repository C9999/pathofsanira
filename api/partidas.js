const { authorizePlayer, sheetsRequest, sendError } = require('./_lib/google');

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Método não permitido.' });
  }
  try {
    const user = await authorizePlayer(req.body?.credential);
    const partida = req.body?.partida || {};
    const id = String(partida.id || '');
    const score = Number(partida.score);
    const elapsedMs = Number(partida.elapsedMs);
    const level = Number(partida.level);
    const dreams = Number(partida.dreams);
    const cards = Array.isArray(partida.cards) ? partida.cards : [];

    if (!/^[a-zA-Z0-9_-]{12,100}$/.test(id) ||
        !Number.isSafeInteger(score) || score < 0 ||
        !Number.isSafeInteger(elapsedMs) || elapsedMs < 0 ||
        !Number.isSafeInteger(level) || level < 1 ||
        !Number.isSafeInteger(dreams) || dreams < 0 ||
        cards.length > 20 || cards.some(card => typeof card !== 'string' || card.length > 80)) {
      return res.status(400).json({ error: 'Os dados da partida são inválidos.' });
    }

    const existing = await sheetsRequest('partidas!A:A');
    if ((existing.values || []).some(row => String(row[0] || '') === id)) {
      return res.status(200).json({ saved: true, duplicate: true });
    }

    const values = [[
      id,
      new Date().toISOString(),
      user.sub,
      user.email,
      user.name,
      score,
      elapsedMs,
      level,
      dreams,
      JSON.stringify(cards)
    ]];
    await sheetsRequest('partidas!A:J', {
      method: 'POST',
      append: true,
      body: { values }
    });
    return res.status(201).json({ saved: true, duplicate: false });
  } catch (error) {
    return sendError(res, error);
  }
};
