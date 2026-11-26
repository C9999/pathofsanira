const { authorizePlayer, sendError } = require('./_lib/google');

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Método não permitido.' });
  }
  try {
    const user = await authorizePlayer(req.body?.credential);
    return res.status(200).json({ user });
  } catch (error) {
    return sendError(res, error);
  }
};
