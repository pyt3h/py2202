
<script>
  let productList = [
    {id: 1, name: 'IPhone X'},
    {id: 2, name: 'IPhone 11'},
    {id: 3, name: 'IPhone 12'},
    {id: 4, name: 'IPhone 13'},
  ];
</script>

<div class="container mt-3">
  <table class="table">
    <tbody>
      <tr>
        <td>Sản phẩm:</td>
        <td>
          <select class='form-control'>
            <option value=""></option>
            {#each productList as product}
              <option value={product.id}>{product.name}</option>
            {/each}
          </select>
        </td>
      </tr>
    </tbody>
  </table>
</div>