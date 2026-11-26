module.exports = async function handler(req, res) {
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'Método não permitido.' });
  }
  const clientId = process.env.GOOGLE_CLIENT_ID;
  if (!clientId) return res.status(503).json({ error: 'Login Google ainda não configurado.' });
  res.setHeader('Cache-Control', 'no-store');
  return res.status(200).json({ googleClientId: clientId });
};
