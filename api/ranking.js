const { authorizePlayer, sheetsRequest, sendError } = require('./_lib/google');

module.exports = async function handler(req, res) {
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'Método não permitido.' });
  }
  try {
    const credential = String(req.headers.authorization || '').replace(/^Bearer\s+/i, '');
    await authorizePlayer(credential);
    const data = await sheetsRequest('partidas!A:J');
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
      cards: (() => { try { return JSON.parse(row[9] || '[]'); } catch { return []; } })()
    })).sort((a, b) => (b.score - a.score) || (b.elapsedMs - a.elapsedMs));
    return res.status(200).json({ partidas });
  } catch (error) {
    return sendError(res, error);
  }
};
