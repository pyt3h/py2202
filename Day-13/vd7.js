let product_list = [
    {'code': 'IPX', 'name': 'IPhone X', 'price': 9.5},
    {'code': 'IP11', 'name': 'IPhone 11', 'price': 11.5},
    {'code': 'IP12', 'name': 'IPhone 12', 'price': 12.5},
    {'code': 'S6', 'name': 'Galaxy S6', 'price': 8.5},
];

let keyword = 'IPhone';
let price_min = 10;
let price_max = 15;

let result = [];

for(let i = 0; i < product_list.length; i++) {
    let product = product_list[i];

    if(!product.name.includes(keyword))
        continue;
    
    if (price_min <= product.price && product.price < price_max)
        result.push(product.name);
}

result = product_list.filter(p => p.name.includes(keyword))
                     .filter(p => p.price >= price_min)
                     .filter(p => p.price < price_max)
                     .map(p => p.name);

console.log('result=', result)