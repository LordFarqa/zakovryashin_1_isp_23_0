const filtersData = {
  category: [],
  brand: [],
  priceRange: ["<100", "100-500", ">500"],
  ratingMin: ["3", "4", "4.5"],
};
let allProducts = [];
let filteredProducts = [];
let currentPage = 1;
const productsPerPage = 14;
const searchHistory = JSON.parse(localStorage.getItem('searchHistory')) || [];
document.addEventListener('DOMContentLoaded', initApp);

async function initApp() {
  await loadProducts();
  setupSearch();
  renderFilters();
  renderProducts();
  document.getElementById('resetFilters').addEventListener('click', resetFilters);
}

async function loadProducts() {
  const response = await fetch('/api/products');
  const { products } = await response.json();
  allProducts = products;
  
  filtersData.category = [...new Set(products.map(p => p.category))];
  filtersData.brand = [...new Set(products.map(p => p.brand))];
  
  filteredProducts = [...allProducts];
}

function setupSearch() {
  const searchInput = document.getElementById('search');
  const searchHistoryEl = document.getElementById('search-history');
  
  searchInput.addEventListener('input', () => {
    currentPage = 1;
    applyFilters();
  });
  
  searchInput.addEventListener('focus', () => {
    renderSearchHistory();
    searchHistoryEl.style.display = 'block';
  });
  
  document.addEventListener('click',(e) => {
    if (!searchInput.contains(e.target) && !searchHistoryEl.contains(e.target)){
      searchHistoryEl.style.display = 'none';
    }
  });
  
  searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && searchInput.value.trim()) {
      addToSearchHistory(searchInput.value.trim());
      applyFilters();
    }
  });
}

function addToSearchHistory(term) {
  const index = searchHistory.indexOf(term);
  if (index !== -1) {
    searchHistory.splice(index, 1);
  }
  
  searchHistory.unshift(term);
  
  if (searchHistory.length > 10) {
    searchHistory.pop();
  }
  
  localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
}

function renderSearchHistory() {
  const searchHistoryEl = document.getElementById('search-history');
  if (searchHistory.length === 0) {
    searchHistoryEl.innerHTML = '<div class="search-history-item">История поиска пуста</div>';
    return;
  }
  
  searchHistoryEl.innerHTML = searchHistory.map(term => `
    <div class="search-history-item" data-term="${term}">${term}</div>
  `).join('');
  document.querySelectorAll('.search-history-item').forEach(item => {
    item.addEventListener('click', () => {
      document.getElementById('search').value = item.dataset.term;
      applyFilters();
      document.getElementById('search-history').style.display = 'none';
    });
  });
}

function renderFilters() {
  const container = document.getElementById('filters-dropdown');
  container.innerHTML = Object.entries(filtersData)
    .map(([key, values]) => `
      <div class="filter-group">
        <label>${getFilterLabel(key)}</label>
        <select id="${key}">
          <option value="">Все</option>
          ${values.map(v => `<option value="${v}">${v}</option>`).join('')}
        </select>
      </div>
    `).join('');
    
  container.querySelectorAll('select').forEach(select => {
    select.addEventListener('change', applyFilters);
  });
  
  const filtersButton = document.getElementById('filters-button');
  filtersButton.addEventListener('click', toggleFiltersDropdown);
  

  document.addEventListener('click', (e) => {
    if (!filtersButton.contains(e.target) && !container.contains(e.target)) {
      container.style.display = 'none';
    }
  });
}

function toggleFiltersDropdown() {
  const dropdown = document.getElementById('filters-dropdown');
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
}

function getFilterLabel(key) {
  const labels = {
    category: 'Категория',
    brand: 'Бренд',
    priceRange: 'Цена',
    ratingMin: 'Рейтинг',
  };
  return labels[key] || key;
}

function resetFilters() {
  document.querySelectorAll('#filters-dropdown select').forEach(select => {
    select.value = '';
  });
  document.getElementById('search').value = '';
  currentPage = 1;
  applyFilters();
}

function applyFilters() {
  const searchTerm = document.getElementById('search').value.toLowerCase();
  const activeFilters = getActiveFilters();
  
  const filtersButton = document.getElementById('filters-button');
  filtersButton.textContent = `Filters ${Object.keys(activeFilters).length}`;
  
  renderActiveFilters(activeFilters);
  
  filteredProducts = allProducts.filter(product => {
    if (searchTerm && !product.title.toLowerCase().includes(searchTerm)) {
      return false;
    }
    
    for (const [key, value] of Object.entries(activeFilters)) {
      if (!checkFilterMatch(key, value, product)) {
        return false;
      }
    }
    
    return true;
  });
  
  renderProducts();
}

function getActiveFilters() {
  const active = {};
  
  for (const key of Object.keys(filtersData)) {
    const select = document.getElementById(key);
    const value = select.value;
    
    if (value) {
      active[key] = value;
    }
  }
  
  return active;
}

function renderActiveFilters(activeFilters) {
  const container = document.getElementById('active-filters');
  container.innerHTML = '';
  
  Object.entries(activeFilters).forEach(([key, value]) => {
    const chip = document.createElement('div');
    chip.className = 'filter-chip';
    chip.innerHTML = `
      <span class="chip-label">${getFilterLabel(key)}: ${value}</span>
      <button class="remove-btn" data-key="${key}">×</button>
    `;
    container.appendChild(chip);
  });
  document.querySelectorAll('.remove-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const key = this.dataset.key;
      document.getElementById(key).value = '';
      applyFilters();
    });
  });
}

function checkFilterMatch(filterKey, filterValue, product) {
  switch(filterKey) {
    case 'priceRange':
      return (
        filterValue === '<100' ? product.price < 100 :
        filterValue === '>500' ? product.price > 500 :
        product.price >= 100 && product.price <= 500
      );
      
    case 'ratingMin':
      return product.rating >= parseFloat(filterValue);
      
    default:
      return product[filterKey] === filterValue;
  }
}

function renderProducts() {
  const startIndex = (currentPage - 1) * productsPerPage;
  const pageProducts = filteredProducts.slice(startIndex, startIndex + productsPerPage);
  const productsContainer = document.getElementById('products');
  
  productsContainer.innerHTML = pageProducts.map(product => `
    <div class="card">
      <img src="${product.thumbnail}" alt="${product.title}">
      <div class="card-body">
        <h3>${product.title}</h3>
        <div class="price">$${product.price}</div>
      </div>
      <div class="view-button" data-id="${product.id}"></div>
    </div>
  `).join('');
  
  setupProductClickHandlers();
  renderPagination();
}

function setupProductClickHandlers() {
  document.querySelectorAll('.view-button').forEach(button => {
    button.addEventListener('click', function() {
      location.href = `/product.html?id=${this.dataset.id}`;
    });
  });
}

function renderPagination() {
  const totalPages = Math.ceil(filteredProducts.length / productsPerPage);
  const pagination = document.getElementById('pagination');
  
  if (totalPages <= 1) {
    pagination.innerHTML = '';
    return;
  }

  let dotsHTML = '';
  for (let i = 1; i <= totalPages; i++) {
    const activeClass = i === currentPage ? 'active' : '';
    dotsHTML += `<button class="pagination-dot ${activeClass}" onclick="goToPage(${i})">${i}</button>`;
  }
  
  pagination.innerHTML = `
    <button class="pagination-btn" ${currentPage === 1 ? 'disabled' : ''} onclick="goToPage(${currentPage - 1})">
      &lt;back
    </button>
    <div class="pagination-dots">${dotsHTML}</div>
    <button class="pagination-btn" ${currentPage === totalPages ? 'disabled' : ''} onclick="goToPage(${currentPage + 1})">
      next&gt;
    </button>
    ${currentPage === totalPages ? '' : `
      <div class="pagination-go-container" onclick="goToPage(${totalPages})">
        <span class="pagination-page-part">page ${totalPages}</span>
        <span class="pagination-go-part">go</span>
      </div>
    `}
  `;
}
function goToPage(page) {
  currentPage = page;
  renderProducts();
}