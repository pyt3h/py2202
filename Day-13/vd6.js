let lst = [1, 2, 3, 4, 5];
let lst_square = lst.map(x => x*x);
console.log(lst_square); // [1, 4, 9, 16, 25]

lst = [1, 2, 3, 4, 5];
let odd_numbers = lst.filter(x => x%2==1);
console.log(odd_numbers); // [1, 3, 5]

let odd_number_squares = lst
                            .filter(x => x%2==1)
                            .map(x => x*x);

odd_number_squares = [];
for(let i = 0; i < lst.length; i++){
    let x = lst[i];
    if(x%2 == 1) odd_number_squares.push(x*x);
}

console.log(odd_number_squares);