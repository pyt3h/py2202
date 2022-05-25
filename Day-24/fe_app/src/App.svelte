<script>
  let customer = {};
  let baseUrl = "http://127.0.0.1:8000/api";

  let cartItemList =[];

  function addCartItem() {
    cartItemList = [...cartItemList, {qty:1}];
  }

  function deleteCartItem(index) {
    cartItemList.splice(index, 1);
    cartItemList = [...cartItemList];
  }

  function getCustomerInfo(e) {
    //alert(e.target.value);
    let url = baseUrl + '/get-customer-by-phone/' + e.target.value;
    console.log('url=', url);
    fetch(url).then(resp => resp.json()).then(result => customer = result);
    //let resp = await fetch(url);
    //customer = await resp.json();
  }

  async function getProductInfo(index, e) {
    let code = e.target.value;
    //alert(code);
    let url = baseUrl + "/get-product-by-code/" + code;
    let resp = await fetch(url);
    let product = await resp.json();
    let cartItem = cartItemList[index];
    cartItem.product_id = product.id;
    cartItem.product_code = product.code;
    cartItem.product_name = product.name;
    cartItem.qty = 1;
    cartItem.price = cartItem.sub_total = product.price;
    cartItemList = [...cartItemList];
  }

  function updateCartItemQty(index, e) {
    let cartItem = cartItemList[index];
    cartItem.qty = e.target.value;
    cartItem.sub_total = cartItem.qty * cartItem.price;
    cartItemList = [...cartItemList];
  }
</script>
<main>
  <div class="container mt-3">
    <h4>Thông tin khách hàng</h4>
    <hr/>
    <table class="table">
      <tbody>
        <tr>
          <th style="width:30%">Số điện thoại:</th>
          <td><input on:change={getCustomerInfo} class="form-control"/></td>
        </tr>
        <tr>
          <th>Họ tên khách hàng:</th>
          <td>{customer.fullname ?? ""}</td>
        </tr>
        <tr>
          <th>Địa chỉ:</th>
          <td>{customer.address ?? ""}</td>
        </tr>
      </tbody>
    </table>
    <br/>
    <h4>Danh sách các mặt hàng mua</h4>
    <hr/>
    <button on:click={addCartItem} class="btn btn-sm btn-primary float-end">Thêm</button>
    <table class="table">
      <thead>
        <tr>
          <th style="width:20%">Mã SP</th>
          <th style="width:25%">Tên SP</th>
          <th style="width:20%">Đơn giá</th>
          <th style="width:10%">Số lượng</th>
          <th style="width:20%">Thành tiền</th>
          <th style="width:5%"></th>
        </tr>
      </thead>
      <tbody>
        {#each cartItemList as cartItem, index}
          <tr>
            <td>
              <input class="form-control" on:change={(e)=>getProductInfo(index,e)}/>
            </td>
            <td>{cartItem.product_name ?? ''}</td>
            <td>{cartItem.price ?? ''}</td>
            <td>
              <input class="form-control" type="number" min="1" value={cartItem.qty}
                on:change={(e)=> updateCartItemQty(index, e)}/>
            </td>
            <td>{cartItem.sub_total ?? ''}</td>
            <td>
              <button on:click={() => deleteCartItem(index)} class="btn btn-danger btn-sm">Xoá</button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
    <div>Tổng số tiền: 12500đ</div>
    <button class="btn btn-primary mt-3">Lưu lại</button>
  </div>
  
</main>