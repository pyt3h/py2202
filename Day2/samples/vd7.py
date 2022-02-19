'''
Dân số Việt Nam năm 2020 là 97.5 triệu người. 
Nếu tốc độ tăng dân số là 1.1% năm thì đến năm bao nhiêu dân số đạt mức 120 triệu
'''

year = 2020
population = 97.5

while population < 120:
    year += 1
    population *= 1 + 1.1/100

print(year, population)