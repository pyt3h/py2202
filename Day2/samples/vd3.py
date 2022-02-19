'''
Các quốc gia được phân loại theo GDP bình quân đầu người theo các mức độ:
    ○ Thu nhập thấp : GDP đầu người < $1026/năm
    ○ Thu nhập trung bình thập: GDP đầu người $1026 ~ $3995/năm
    ○ Thu nhập trung bình cao: GDP đầu người $3995 ~ $12375/năm
    ○ Thu nhập cao: GDP đầu người > $12375/năm

Nhập vào từ bàn phím điểm đánh giá TB của một sản phẩm, in ra sản phẩm thuộc nhóm nào
'''

gdp = input('GDP bình quân đầu người:')
gdp = float(gdp)

if gdp < 1026:
    print('Quốc gia thu nhập thấp')

elif gdp < 3995:
    print('Quốc gia thu nhập trung bình thấp')

elif gdp < 12375:
    print('Quốc gia thu nhập trung bình cao')

else:
    print('Quốc gia thu nhập cao')
