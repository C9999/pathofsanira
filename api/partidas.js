const {
  authorizePlayer,
  sheetsRequest,
  sheetsBatchUpdate,
  getSheetId,
  sendError
} = require('./_lib/google');

function normalizeHex(value) {
  const match = /^#?([0-9a-f]{6})$/i.exec(String(value || '').trim());
  return match ? '#' + match[1].toUpperCase() : '';
}

function hexToRgb(hex) {
  const value = normalizeHex(hex);
  if (!value) return null;
  return {
    red: parseInt(value.slice(1, 3), 16) / 255,
    green: parseInt(value.slice(3, 5), 16) / 255,
    blue: parseInt(value.slice(5, 7), 16) / 255
  };
}

function colorsFromRow(row) {
  let cards = [];
  try {
    cards = JSON.parse(String(row[9] || '[]'));
  } catch (_) {
    cards = [];
  }
  return [0, 1, 2].map(index => normalizeHex(cards[index]));
}

function colorFormatRequests(sheetId, rowNumber, colors) {
  const requests = [];
  colors.forEach((hex, index) => {
    const rgb = hexToRgb(hex);
    if (!rgb) return;
    const luminance = rgb.red * 0.299 + rgb.green * 0.587 + rgb.blue * 0.114;
    requests.push({
      repeatCell: {
        range: {
          sheetId,
          startRowIndex: rowNumber - 1,
          endRowIndex: rowNumber,
          startColumnIndex: 10 + index,
          endColumnIndex: 11 + index
        },
        cell: {
          userEnteredFormat: {
            backgroundColor: rgb,
            horizontalAlignment: 'CENTER',
            verticalAlignment: 'MIDDLE',
            textFormat: {
              foregroundColor: luminance > 0.62
                ? { red: 0.12, green: 0.12, blue: 0.12 }
                : { red: 1, green: 1, blue: 1 },
              bold: true
            }
          }
        },
        fields: 'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)'
      }
    });
  });
  return requests;
}

function rowNumberFromAppend(result, fallback) {
  const range = result?.updates?.updatedRange || '';
  const match = /![A-Z]+(\\d+):/.exec(range);
  return match ? Number(match[1]) : fallback;
}

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

    const headerData = await sheetsRequest('partidas!A1:M1');
    const headers = headerData.values?.[0] || [];
    if (!headers[10] || !headers[11] || !headers[12]) {
      await sheetsRequest('partidas!K1:M1', {
        method: 'PUT',
        body: { values: [['Carta 1', 'Carta 2', 'Carta 3']] }
      });
    }

    const existing = await sheetsRequest('partidas!A:M');
    const rows = existing.values || [];
    if (rows.slice(1).some(row => String(row[0] || '') === id)) {
      return res.status(200).json({ saved: true, duplicate: true });
    }

    // Migra uma única vez as partidas antigas que ainda não têm as colunas visuais.
    const historicalRows = rows.slice(1);
    const needsBackfill = historicalRows.some(row =>
      row[9] && (!row[10] || !row[11] || !row[12])
    );
    const sheetId = await getSheetId('partidas');
    if (needsBackfill) {
      const values = historicalRows.map(row => colorsFromRow(row));
      await sheetsRequest('partidas!K2:M' + (historicalRows.length + 1), {
        method: 'PUT',
        body: { values }
      });
      const formatRequests = [];
      values.forEach((colors, index) => {
        formatRequests.push(...colorFormatRequests(sheetId, index + 2, colors));
      });
      if (formatRequests.length) await sheetsBatchUpdate(formatRequests);
    }

    const cardColors = [0, 1, 2].map(index => normalizeHex(cards[index]));
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
      JSON.stringify(cards),
      cardColors[0],
      cardColors[1],
      cardColors[2]
    ]];
    const appendResult = await sheetsRequest('partidas!A:M', {
      method: 'POST',
      append: true,
      body: { values }
    });
    const rowNumber = rowNumberFromAppend(appendResult, rows.length + 1);
    const formatRequests = colorFormatRequests(sheetId, rowNumber, cardColors);
    if (formatRequests.length) await sheetsBatchUpdate(formatRequests);

    return res.status(201).json({ saved: true, duplicate: false, colorsFormatted: true });
  } catch (error) {
    return sendError(res, error);
  }
};
