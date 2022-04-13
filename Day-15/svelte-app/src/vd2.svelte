<script>
  let a='';    // số thứ nhất
  let b='';    // số thứ hai
  let c='';    // tổng
  function calcSum() {
    c = parseFloat(a) + parseFloat(b);
  }
</script>

<div>
  <table>
    <tbody>
      <tr>
        <td>Số thứ nhất: </td>
        <td><input on:change={e => a = e.target.value}/></td>
      </tr>
      <tr>
        <td>Số thứ hai: </td>
        <td><input on:change={e => b = e.target.value}/></td>
      </tr>
    </tbody>
  </table>
  <button on:click={calcSum}>Tính tổng</button>
  <span>Tổng:{c}</span>
</div>