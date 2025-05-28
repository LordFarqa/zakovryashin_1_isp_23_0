let express = require('express');
let path    = require('path');
let axios   = require('axios');

let app = express();
let PORT = process.env.PORT || 3000;

let PUBLIC_DIR = path.join(__dirname, 'public');

app.get('/api/products', async (req, res) => {
  try {
    let { data } = await axios.get('https://dummyjson.com/products');
    res.json(data);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: 'Cannot fetch products' });
  }
});

app.get('/api/products/:id', async (req, res) => {
  try {
    let { id } = req.params;
    let { data } = await axios.get(`https://dummyjson.com/products/${id}`);
    res.json(data);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: 'Cannot fetch product' });
  }
});

app.use(express.static(PUBLIC_DIR, { index: false }));
app.get('/', (req, res) => {
  res.sendFile(path.join(PUBLIC_DIR, 'index.html'));
});
app.get('/product.html', (req, res) => {
  res.sendFile(path.join(PUBLIC_DIR, 'product.html'));
});

app.use((req, res) => {
  res.status(404).send(`
    <h1>404 — Не найдено</h1>
    <p>Адрес <code>${req.originalUrl}</code> отсутствует на сервере.</p>
    <a href="/">Вернуться на главную</a>
  `);
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
