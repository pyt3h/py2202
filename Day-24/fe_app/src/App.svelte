<script>
  let customer = {};
  let baseUrl = "http://127.0.0.1:8000/api";
  function getCustomerInfo(e) {
    //alert(e.target.value);
    let url = baseUrl + '/get-customer-by-phone/' + e.target.value;
    console.log('url=', url);
    fetch(url).then(resp => resp.json()).then(result => customer = result);
    //let resp = await fetch(url);
    //customer = await resp.json();
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
    <button class="btn btn-sm btn-primary float-end">Thêm</button>
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
        <tr>
          <td>
            <input class="form-control"/>
          </td>
          <td>Mỳ hảo hảo chua cay</td>
          <td>3500</td>
          <td><input class="form-control" type="number" min="1"/></td>
          <td>3500</td>
          <td>
            <button class="btn btn-danger btn-sm">Xoá</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div>Tổng số tiền: 12500đ</div>
    <button class="btn btn-primary mt-3">Lưu lại</button>
  </div>
  
</main>