'''
Cho một dãy số, kiểm tra dãy số có theo thứ tự tăng dần không
'''

ds = [2, 3, 4, 5, 6, 2]

n = len(ds)
for i in range(n-1):
    if ds[i] > ds[i+1]:
        print('Dãy số không theo thứ tự tăng dần')
        break
else:
    print('Dãy số theo thứ tự tăng dần')
