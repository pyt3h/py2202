
<div class="container mt-3">
  <h3>Thời tiết 24h tới</h3>
  <table class="table table-bordered">
      <thead>
          <tr>
              <th>Thời gian</th>
              <th>Nhiệt độ °C</th>
              <th>Độ ẩm (%)</th>
              <th>Áp suất khí quyển (atm)</th>
          </tr>
      </thead>
      <tbody id="table_body">
        {#each data as row}
          <tr>
            <td>{row?.time ?? '-'}</td>
            <td>{row?.main?.temp ?? '-'}</td>
            <td>{row?.main?.humidity ?? '-'}</td>
            <td>{row?.main?.pressure ?? '-'}</td>
          </tr>
        {/each}
      </tbody>
  </table>
</div>
<script>
  let url = 'http://api.openweathermap.org/data/2.5/forecast?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9&cnt=8';
  let data = [];
  /*   
  fetch(url)
      .then(resp => resp.json())
      .then(data => console.log(data));
  */

  async function init() {
      let resp = await fetch(url);
      data = await resp.json();
      data = data.list.map(item => ({main: item.main, time: item.dt_txt}));
      console.log(data);
  }
  
  init(); //main
</script>