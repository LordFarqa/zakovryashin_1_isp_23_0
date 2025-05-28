
let express = require('express');
let path    = require('path');
let fs      = require('fs');

let router = express.Router();
let PUB = path.join(__dirname, '..', 'public');

router.get('/', (req, res) => {
  res.sendFile(path.join(PUB, 'index.html'));
});

router.get('/product.html', (req, res) => {
  res.sendFile(path.join(PUB, 'product.html'));
});
let fetch = require('node-fetch');
let API_URL = 'https://dummyjson.com/products';

router.get('/api/products', async (req, res) => {
  try {
    let apiRes = await fetch(API_URL);
    let data   = await apiRes.json();
    res.json(data);
  } catch (e) {
    res.status(500).json({ error: 'API fetch error' });
  }
});
router.get('/api/products/:id', async (req, res) => {
  try {
    let apiRes = await fetch(`${API_URL}/${req.params.id}`);
    let data   = await apiRes.json();
    res.json(data);
  } catch (e) {
    res.status(500).json({ error: 'API fetch error' });
  }
});
router.use('/css', express.static(path.join(PUB, 'css')));
router.use('/js',  express.static(path.join(PUB, 'js')));


router.use((req, res) => {
  res.status(404).send(`
    <h1>404 — Не найдено</h1>
    <p>Адрес <code>${req.originalUrl}</code> отсутствует на сервере.</p>
    <a href="/">Вернуться на главную</a>
  `);
});

module.exports = router;
