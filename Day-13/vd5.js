let temp_table = [
    {hour: 0, temp: 20},
    {'hour': 2, 'temp': 20},
    {'hour': 4, 'temp': 19},
    {'hour': 6, 'temp': 20},
    {'hour': 8, 'temp': 21},
    {'hour': 10, 'temp': 23},
    {'hour': 12, 'temp': 24},
    {'hour': 14, 'temp': 25},
    {'hour': 16, 'temp': 24},
    {'hour': 18, 'temp': 22},
    {'hour': 20, 'temp': 21},
    {'hour': 22, 'temp': 19},
];

let temp_max = temp_table[0].temp;
let hour_max = 0;

for(let i = 0; i < temp_table.length;i++){
    let record = temp_table[i];
    if(record.temp > temp_max){
        temp_max = record.temp;
        hour_max = record.hour;
    }
}

console.log(`Nhiệt độ cao nhất : ${temp_max} độ, lúc ${hour_max}h`)