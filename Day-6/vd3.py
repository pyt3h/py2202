# Đọc vào một file văn bản, tạo ra một file văn bản mới bằng cách bỏ đi các dòng trống.
infile = open('input.txt', encoding='utf-8')
outfile = open('output.txt', 'w', encoding='utf-8')

for line in infile:
    if line.strip() != '':
        outfile.write(line)

infile.close()
outfile.close()