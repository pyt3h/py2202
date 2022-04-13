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
            <tr>...</tr>
          {/each}
        </tbody>
    </table>
</div>

<script>
    let data = [
        {time: '2022-03-25 15:00:00', temp: 24.5, humdity: 88, pressure: 1.008},
        {time: '2022-03-25 18:00:00', temp: 24.17, humdity: 91, pressure: 1.007},
        {time: '2022-03-25 21:00:00', temp: 23.12, humdity: 92, pressure: 1.009},
        {time: '2022-03-26 00:00:00', temp: 22.26, humdity: 90, pressure: 1.012},
    ];
    /*
    function renderRow(row){
        return (`
            <tr>	
                <td>${row.time}</td>
                <td>${row.temp}</td>
                <td>${row.humdity}</td>
                <td>${row.pressure}</td>
            </tr>`
        );
    };
    let html = data.map(renderRow).join('');
    document.getElementById('table_body').innerHTML = html;*/
</script>