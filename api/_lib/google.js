const { OAuth2Client, JWT } = require('google-auth-library');
const SHEET_ID = process.env.GOOGLE_SHEET_ID;

function requiredEnv() {
  for (const key of ['GOOGLE_CLIENT_ID', 'GOOGLE_SERVICE_ACCOUNT_EMAIL', 'GOOGLE_PRIVATE_KEY', 'GOOGLE_SHEET_ID']) {
    if (!process.env[key]) throw new Error('Configuração ausente no servidor: ' + key);
  }
}

function serviceAccount() {
  requiredEnv();
  return new JWT({
    email: process.env.GOOGLE_SERVICE_ACCOUNT_EMAIL,
    key: process.env.GOOGLE_PRIVATE_KEY.replace(/\\n/g, '\n'),
    scopes: ['https://www.googleapis.com/auth/spreadsheets']
  });
}

async function sheetsRequest(range, options = {}) {
  const auth = serviceAccount();
  const { token } = await auth.getAccessToken();
  if (!token) throw new Error('Não foi possível autenticar a conta de serviço.');
  const baseUrl = 'https://sheets.googleapis.com/v4/spreadsheets/' + encodeURIComponent(SHEET_ID) +
    '/values/' + encodeURIComponent(range);
  const url = options.append
    ? baseUrl + ':append?valueInputOption=RAW&insertDataOption=INSERT_ROWS'
    : baseUrl;
  const response = await fetch(url, {
    method: options.method || 'GET',
    headers: {
      Authorization: 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: options.body ? JSON.stringify(options.body) : undefined
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error(data.error?.message || 'Erro ao acessar Google Sheets.');
    error.statusCode = response.status;
    throw error;
  }
  return data;
}

async function verifyGoogleCredential(credential) {
  requiredEnv();
  if (typeof credential !== 'string' || !credential) {
    const error = new Error('Faça login com sua conta Google.');
    error.statusCode = 401;
    throw error;
  }
  const oauthClient = new OAuth2Client(process.env.GOOGLE_CLIENT_ID);
  const ticket = await oauthClient.verifyIdToken({
    idToken: credential,
    audience: process.env.GOOGLE_CLIENT_ID
  });
  const payload = ticket.getPayload();
  if (!payload || !payload.sub || !payload.email || payload.email_verified !== true) {
    const error = new Error('Não foi possível confirmar sua conta Google.');
    error.statusCode = 401;
    throw error;
  }
  const issuer = payload.iss;
  if (issuer !== 'accounts.google.com' && issuer !== 'https://accounts.google.com') {
    const error = new Error('Emissor do login Google inválido.');
    error.statusCode = 401;
    throw error;
  }
  return {
    sub: payload.sub,
    email: String(payload.email).trim().toLowerCase(),
    name: payload.name || payload.given_name || payload.email.split('@')[0]
  };
}

async function authorizePlayer(credential) {
  const user = await verifyGoogleCredential(credential);
  const data = await sheetsRequest('jogadoras!A:C');
  const rows = data.values || [];
  const registered = rows.slice(1).filter(row => String(row[0] || '').trim());
  const players = registered.filter(row => String(row[2] || '').toUpperCase() === 'TRUE');
  if (registered.length > 50) {
    const error = new Error('O cadastro ultrapassou o limite de 50 jogadoras ativas. Procure a administração.');
    error.statusCode = 503;
    throw error;
  }
  const player = players.find(row => String(row[0] || '').trim().toLowerCase() === user.email);
  if (!player) {
    const error = new Error('Este e-mail não está autorizado a acessar o Path of Sanira.');
    error.statusCode = 403;
    throw error;
  }
  return { ...user, name: String(player[1] || user.name).trim() };
}


async function sheetsBatchUpdate(requests) {
  const auth = serviceAccount();
  const { token } = await auth.getAccessToken();
  if (!token) throw new Error('Não foi possível autenticar a conta de serviço.');
  const url = 'https://sheets.googleapis.com/v4/spreadsheets/' + encodeURIComponent(SHEET_ID) + ':batchUpdate';
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ requests })
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error(data.error?.message || 'Erro ao formatar a planilha.');
    error.statusCode = response.status;
    throw error;
  }
  return data;
}

async function getSheetId(title) {
  const auth = serviceAccount();
  const { token } = await auth.getAccessToken();
  if (!token) throw new Error('Não foi possível autenticar a conta de serviço.');
  const url = 'https://sheets.googleapis.com/v4/spreadsheets/' + encodeURIComponent(SHEET_ID) +
    '?fields=sheets.properties(sheetId,title)';
  const response = await fetch(url, {
    headers: { Authorization: 'Bearer ' + token }
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error(data.error?.message || 'Erro ao consultar a estrutura da planilha.');
    error.statusCode = response.status;
    throw error;
  }
  const sheet = (data.sheets || []).find(item => item.properties?.title === title);
  if (!sheet) throw new Error('A aba ' + title + ' não foi encontrada.');
  return sheet.properties.sheetId;
}

function sendError(res, error) {
  const status = error.statusCode || 500;
  if (status >= 500) console.error('[Path of Sanira API]', error);
  return res.status(status).json({
    error: status >= 500 ? 'Não foi possível concluir a operação. Tente novamente.' : error.message
  });
}

module.exports = { authorizePlayer, sheetsRequest, sheetsBatchUpdate, getSheetId, sendError };
