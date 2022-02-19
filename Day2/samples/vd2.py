'''
Nhập vào 3 số từ bàn phím, kiểm tra 3 số có phải là cạnh 1 tam giác không
'''

a = input('a=')
a = float(a)

b = input('b=')
b = float(b)

c = input('c=')
c = float(c)

if a + b > c and b + c > a and c + a > b:
    print(a, b, c, 'là 3 cạnh một tam giác')
else:
    print(a, b, c, 'không phải 3 cạnh một tam giác')
