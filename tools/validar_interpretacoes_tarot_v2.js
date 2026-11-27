#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');

const file = process.argv[2] || path.join(__dirname, '..', 'data', 'interpretacoes-tarot.json');
const indexFile = path.join(__dirname, '..', 'index.html');
const data = JSON.parse(fs.readFileSync(file, 'utf8'));
const html = fs.readFileSync(indexFile, 'utf8');
const ids = ['louco','mago','sacer','imper','carro','forca','eremita','roda','morte','torre','lua','sol'];
const canonicalIds = Object.keys(data.cartas);
assert.deepEqual(canonicalIds, ids, 'A ordem canônica das 12 cartas mudou');

const expectedKeys = [];
for (let a = 0; a < ids.length; a++) {
  for (let b = a + 1; b < ids.length; b++) {
    for (let c = b + 1; c < ids.length; c++) expectedKeys.push([ids[a], ids[b], ids[c]].join('_'));
  }
}
const keys = Object.keys(data.combinacoes);
assert.equal(keys.length, 220, 'O JSON deve conter 220 combinações');
assert.deepEqual(keys, expectedKeys, 'As chaves não seguem a ordem canônica esperada');

let permutations = 0;
let totalMessages = 0;
const allMessages = new Set();

function checkPermutations(items, start = 0) {
  if (start === items.length) {
    const key = [...items].sort((a, b) => canonicalIds.indexOf(a) - canonicalIds.indexOf(b)).join('_');
    assert.ok(data.combinacoes[key], 'O algoritmo do jogo não encontrou a combinação: ' + key);
    permutations++;
    return;
  }
  for (let i = start; i < items.length; i++) {
    [items[start], items[i]] = [items[i], items[start]];
    checkPermutations(items, start + 1);
    [items[start], items[i]] = [items[i], items[start]];
  }
}

for (const key of keys) {
  const entry = data.combinacoes[key];
  const cardIds = key.split('_');
  assert.deepEqual(entry.cartas, cardIds, 'Campo cartas divergente da chave: ' + key);
  assert.equal(entry.mensagens.length, 3, 'A combinação deve ter exatamente 3 mensagens: ' + key);
  assert.equal(new Set(entry.mensagens).size, 3, 'Mensagens repetidas na combinação: ' + key);
  for (const message of entry.mensagens) {
    assert.equal(typeof message, 'string');
    assert.ok(!/[{}]/.test(message), 'Placeholder encontrado: ' + key);
    assert.ok(!message.includes('  '), 'Espaço duplo encontrado: ' + key);
    assert.ok(message.endsWith('.'), 'Mensagem sem ponto final: ' + key);
    assert.ok(!allMessages.has(message), 'Mensagem repetida globalmente: ' + key);
    allMessages.add(message);
    totalMessages++;
  }
  checkPermutations([...cardIds]);
}
assert.equal(permutations, 1320, 'Devem ser testadas 1.320 ordens possíveis');
assert.equal(totalMessages, 660, 'Devem existir 660 mensagens distintas');

assert.ok(html.includes('const ordemCartas=Object.keys(tarotData?.cartas||{});'), 'A ordem canônica do jogo mudou');
assert.ok(html.includes('tarotData?.combinacoes?.[tarotKey]?.mensagens||['), 'Fallback genérico para JSON/combinação ausente não foi encontrado');
assert.ok(html.includes('Math.floor(Math.random()*options.length)'), 'Sorteio entre as três mensagens não foi encontrado');

console.log('OK: 220 combinações, 1.320 permutações e 660 mensagens únicas.');
console.log('OK: chaves e cartas na ordem canônica; textos sem placeholders/espaços duplos e com ponto final.');
console.log('OK: seleção aleatória e fallback genérico presentes em index.html.');
