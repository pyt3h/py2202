<script>
  let name;
</script>

<div>
  Tên của bạn: 
  <input on:change={(e) => name = e.target.value}/>
  Xin chào {name}!
</div>