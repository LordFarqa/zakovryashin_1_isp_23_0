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
      <div class="product-main">
        <img src="${p.images?.[0] || p.thumbnail}" alt="${p.title}">
        <div class="product-info">
          <h1>${p.title}</h1>
          <div class="price">$${p.price}</div>
          <div class="meta">
            <span>Категория: ${p.category}</span>
            <span>Бренд: ${p.brand}</span>
            <span>Рейтинг: ${p.rating}</span>
          </div>
          <p><strong>Описание:</strong> ${p.description}</p>
          <a href="/" class="view-button">Вернуться в каталог</a>
        </div>
      </div>
      <div class="product-description">
        <h2>Дополнительная информация</h2>
        <p>${p.description}</p>
        <p>Этот товар имеет рейтинг ${p.rating} из 5 и относится к категории ${p.category}.</p>
      </div>
    `;
  }
});