const { authorizePlayer, sheetsRequest, sendError } = require('./_lib/google');

module.exports = async function handler(req, res) {
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'Método não permitido.' });
  }
  try {
    const credential = String(req.headers.authorization || '').replace(/^Bearer\s+/i, '');
    await authorizePlayer(credential);
    const data = await sheetsRequest('partidas!A:M');
    const rows = (data.values || []).slice(1).filter(row => row[0]);
    const partidas = rows.map(row => ({
      id: String(row[0]),
      createdAt: String(row[1] || ''),
      email: String(row[3] || ''),
      name: String(row[4] || 'Jogadora'),
      score: Number(row[5]) || 0,
      elapsedMs: Number(row[6]) || 0,
      level: Number(row[7]) || 1,
      dreams: Number(row[8]) || 0,
      cards: (() => { try { return JSON.parse(row[9] || '[]'); } catch { return []; } })(),
      cardNames: [10, 11, 12].map(index => String(row[index] || ''))
    })).sort((a, b) => (b.score - a.score) || (b.elapsedMs - a.elapsedMs));
    const rankingSecreto = partidas.filter(partida =>
      !(partida.cards || []).some(color => String(color).trim().toUpperCase() === '#F28C28') &&
      !(partida.cardNames || []).some(name => String(name).trim().toLowerCase() === 'a força')
    );
    return res.status(200).json({ partidas, rankingSecreto });
  } catch (error) {
    return sendError(res, error);
  }
};
