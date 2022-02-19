'''
Chỉ số BMI được dùng để đánh giá tình trạng gầy, béo của một người. Chỉ số này được tính theo công thức:
    bmi = w/(h*h)

Trong đó h là chiều cao tính theo đơn vị mét, w là cân nặng tính theo đơn vị kg. Dựa vào chỉ số bmi, một người được đánh giá như sau:
    ○ Gầy: nếu bmi<16
    ○ Hơi gầy: nếu bmi 16 ~ 18.5
    ○ Bình thường: nếu bmi 18.5~25
    ○ Hơibéo: nếubmi25~30
    ○ Béo: nếu bmi > 30
Nhập vào từ bàn phím chiều cao & cân nặng của một người, in ra tình trạng gầy/béo của người đó
'''

height = input('Chiều cao (mét) : ')
height = float(height)

mass = input('Cân nặng (kg) : ')
mass = float(mass)

bmi = mass / (height * height)

if bmi < 16:
    print('Thân hình gầy')

elif bmi < 18.5:
    print('Thân hình hơi gầy')

elif bmi < 25:
    print('Thân hình bình thường')

elif bmi < 30:
    print('Thân hình hơi béo')

else:
    print('Thân hình béo')
