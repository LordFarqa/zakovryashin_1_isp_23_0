document.addEventListener('DOMContentLoaded', () => {
  const container   = document.getElementById('productsContainer');
  const searchInput = document.getElementById('searchInput');
  if (document.getElementById('productDetail')) {
    renderProductDetail();
  } else {
    fetch('/api/products')
      .then(r => r.json())
      .then(data => {
        window.allProducts = data.products;
        renderProducts(data.products);

        searchInput.addEventListener('input', e => {
          const term = e.target.value.toLowerCase();
          const filtered = window.allProducts.filter(p =>
            p.title.toLowerCase().includes(term) ||
            p.category.toLowerCase().includes(term)
          );
          renderProducts(filtered);
        });
      });
  }

  function renderProducts(arr) {
    container.innerHTML = arr.map(p => `
      <div class="product-card">
        <a href="/product.html?id=${p.id}">
          <img src="${p.thumbnail}" alt="${p.title}">
          <h3>${p.title}</h3>
          <p>Категория: ${p.category}</p>
          <p>Цена: $${p.price}</p>
        </a>
      </div>
    `).join('');
  }

  function renderProductDetail() {
    const params = new URLSearchParams(location.search);
    const id     = params.get('id');
    const out    = document.getElementById('productDetail');
    fetch(`/api/products/${id}`)
      .then(r => r.json())
      .then(p => {
        out.innerHTML = `
          <h2>${p.title}</h2>
          <img src="${p.images?.[0] || p.thumbnail}" style="max-width:300px">
          <p>Категория: ${p.category}</p>
          <p>Цена: $${p.price}</p>
          <p>${p.description}</p>
        `;
      });
  }
});
