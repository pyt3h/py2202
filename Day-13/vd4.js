let ds = [1, 2, 3, 5, 7, 8, 9, 10, 11, 15];
let ds_le = [];
let ds_chan = [];

for(let i = 0; i < ds.length; i++) {
    let x = ds[i];
    if(x%2 == 0) {
        ds_chan.push(x);
    }else{
        ds_le.push(x);
    }
}

console.log('Số chẵn:', ds_chan);
console.log('Số lẻ:', ds_le);