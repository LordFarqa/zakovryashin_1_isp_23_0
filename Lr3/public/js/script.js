document.addEventListener('DOMContentLoaded', () => {
  let allProducts = [];
  let searchInput = document.getElementById('searchInput') || document.getElementById('search');
  let container   = document.getElementById('products')   || document.getElementById('productsContainer');
  fetch('/api/products')
    .then(res => res.json())
    .then(data => {
      allProducts = data.products || data;
      renderProducts(allProducts);
    })
    .catch(console.error);
  searchInput.addEventListener('input', (e) => {
    let term = e.target.value.toLowerCase();
    let filtered = allProducts.filter(p =>
      p.title.toLowerCase().includes(term) ||
      p.category.toLowerCase().includes(term)
    );
    renderProducts(filtered);
  });

  function renderProducts(products) {
    container.innerHTML = products.map(product => {
      return `
        <div class="card" data-id="${product.id}">
          <img src="${product.thumbnail}" alt="${product.title}">
          <h3>${product.title}</h3>
          <p>Категория: ${product.category}</p>
          <p>Цена: $${product.price}</p>
        </div>
      `;
    }).join('');
    document.querySelectorAll('.card').forEach(card => {
      card.style.cursor = 'pointer';
      card.onclick = () => {
        let id = card.getAttribute('data-id');
        window.location.href = `/product.html?id=${id}`;
      };
    });
  }
});
