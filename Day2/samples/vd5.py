'''
Cho một dãy số, kiểm tra trong dãy số có chứa số lẻ không
'''
ds = [2, 4, 5, 6, 4, 8]

for x in ds:
    if x % 2 == 1:
        print('Dãy số chứa số lẻ:', x)
        break
else:
    print('Dãy số không chứa số lẻ')