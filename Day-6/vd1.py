#Viết hàm validate mật khẩu, yêu cầu:
# + Độ dài tối thiểu là 6
# + Chứa ít nhất một chữ cái
# + Chứa ít nhất một chữ số

def check_contain_char(st, c_min, c_max):
    for c in st:
        if c_min <= c <= c_max:
            return True

    return False

def validate_password(password):
    if len(password) < 6:
        return False

    if not check_contain_char(password, '0', '9'):
        return False

    return (
        check_contain_char(password, 'a', 'z') or
        check_contain_char(password, 'A', 'Z')
    )

print(validate_password('abc123'))  # Expect: True
print(validate_password('abc12'))   # Expect: False