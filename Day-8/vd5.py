import csv

# Đọc dữ liệu từ file csv
with open('student.csv', encoding='utf-8') as fi:
    reader = csv.reader(fi,delimiter=',')
    header_row = next(reader)   # Dòng tiêu đề 
    data_rows = list(reader)    # Các dòng dữ liệu

print('Header:', header_row)
for row in data_rows:
    hs1, hs2, hs3 = int(row[1]), int(row[2]), int(row[3])
    tb = (hs1 + 2*hs2 + 3*hs3)/6
    row.append(f'{tb:0.2f}')

header_row.append('Điểm TB')
print(header_row)

# Ghi dữ liệu vào file csv
with open('output.csv', 'w', newline='',  encoding='utf-8') as fo:
    writer = csv.writer(fo, delimiter=',')
    writer.writerow(header_row)     # Ghi dòng tiêu đề
    writer.writerows(data_rows)     # Ghi các dòng dữ liệu