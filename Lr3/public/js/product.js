document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('productDetail');

  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');
  if (!id) {
    container.innerHTML = '<p>Не указан ID товара.</p>';
    return;
  }
    fetch(`/api/products/${id}`)
        .then(res => {
        if (!res.ok) throw new Error('Товар не найден');
        return res.json();
        })
        .then(product => {
        renderProduct(product);
        })
        .catch(err => {
        container.innerHTML = `<p>Ошибка: ${err.message}</p>`;
        });
    function renderProduct(p) {
        container.innerHTML = `
        <h1>${p.title}</h1>
        <img src="${p.images?.[0] || p.thumbnail}" alt="${p.title}" style="max-width:300px;">
        <p><strong>Категория:</strong> ${p.category}</p>
        <p><strong>Цена:</strong> $${p.price}</p>
        <p><strong>Описание:</strong> ${p.description}</p>
        <p><strong>Рейтинг:</strong> ${p.rating}</p>
        `;
    }
});
