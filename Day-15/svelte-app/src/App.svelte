<script>
  let url = 'https://raw.githubusercontent.com/pytutorial/themes/master/shop_themes/product_list.json';
  let productList = []; 
  let allProductList = []
  fetch(url).then(resp => resp.json()).then(result => {
    console.log(result);
    allProductList = productList = result;
  });

  let name = '';
  let priceRange = '';
  function search() {
    productList = allProductList.filter(p => p.name.includes(name));
    if(priceRange == 1) {
      productList = productList.filter(p => p.price <= 10000000);
    }
    if(priceRange == 2) {
      productList = productList.filter(p => p.price >= 10000000 && p.price <= 20000000);
    }
    if(priceRange == 3) {
      productList = productList.filter(p => p.price >= 20000000);
    }
  }
</script>

<div>
  <div class="bg-primary">
    <div class="container">
      <nav class="navbar navbar-expand navbar-dark bg-primary p-0">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#/">Sản phẩm</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#/">Liên hệ</a>
          </li>
        </ul>
      </nav>
    </div>
  </div>

  <div class="container mt-5 mb-5">
    <div class="row">
      <div class="col-3 p-3 card">
        <form>
          <div class="product-search-info mt-3">
            <label for="name" class="mb-1"><b>Tên sản phẩm:</b></label>
            <input
              name="name"
              class="form-control"
              placeholder="Nhập tên sản phẩm để tìm"
              on:change={(e) => name = e.target.value}
            />
          </div>

          <div class="category-search-info mt-3">
            <label for="categoryId"><b>Hãng sản xuất:</b></label>
            <div class="mt-2">
              <input type="radio" name="categoryId" checked value="" />
              <span>Tất cả</span>
            </div>
            <div class="mt-1">
              <input name="categoryId" type="radio" value="1" />
              <span>Acer</span>
            </div>
            <div class="mt-1">
              <input name="categoryId" type="radio" value="2" />
              <span>Asus</span>
            </div>
            <div class="mt-1">
              <input name="categoryId" type="radio" value="3" />
              <span>Lenovo</span>
            </div>
          </div>

          <div class="price-search-info mt-3">
            <label for="priceRange"><b>Mức giá:</b></label>
            <div class="mt-2">
              <input type="radio" name="priceRange" checked value="" on:click={() => priceRange=''}/>
              <span>Tất cả</span>
            </div>

            <div class="mt-1">
              <input type="radio" name="priceRange" value="1" on:click={() => priceRange=1}/>
              <span>Dưới 10 triệu</span>
            </div>

            <div class="mt-1">
              <input type="radio" name="priceRange" value="2" on:click={() => priceRange=2}/>
              <span>Từ 10-20 triệu</span>
            </div>

            <div class="mt-1">
              <input type="radio" name="priceRange" value="3" on:click={() => priceRange=3}/>
              <span>Trên 20 triệu</span>
            </div>
          </div>

          <button type="button" on:click={search} class="btn btn-primary mt-4 mb-4">Tìm kiếm</button>
        </form>
      </div>
      <div class="col-9">
        <ul class="list-unstyled row">
          {#each productList as product}
            <li class="list-item col-sm-4 mt-3">
              <div class="item-container">
                <a href="view_product.html?id=1" class="product-item">
                  <img
                    src={product.image}
                    class="product-image"
                    alt=""
                  />
                  <div class="item-info">
                    <div>
                      <span class="product-name">{product.name}</span>
                    </div>
                    <div>
                      <span class="price-title">Giá bán :</span>
                      <span class="price">{product.price} ₫</span>
                    </div>
                  </div>
                </a>
              </div>
            </li>
          {/each}
        </ul>
      </div>
    </div>
  </div>
</div>

<style>
  .product-image {
    width: 95%;
  }

  .price-title {
    font-style: italic;
    font-size: 14px;
  }

  .price {
    font-size: 16px;
    font-weight: bold;
  }

  .product-item,
  .product-item:link,
  .product-item:hover,
  .product-item:visited {
    text-decoration: none;
    color: black;
  }

  .item-container {
    position: relative;
    height: 100%;
    padding-bottom: 50px;
  }

  .item-info {
    position: absolute;
    bottom: 0px;
    height: 50px;
  }
</style>