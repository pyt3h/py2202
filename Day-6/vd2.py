#Nhập vào từ bàn phím 3 số d,m,y. In ra xem ngày d/m/y có tồn tại không
def is_leap_year(y):
    if y % 400 == 0:
        return True
    
    return y%100 != 0 and y%4 == 0

def get_day_in_month(m, y):
    if m == 2:
        if is_leap_year(y):
            return 29
        return 28
    
    if m in [4, 6, 9, 11]:
        return 30

    return 31

def validate_date(d, m, y):
    d_max = get_day_in_month(m, y)
    return (
        y > 0 and 
        1 <= m <= 12 and 
        1 <= d <= d_max
    )
print(validate_date(31, 2, 8))