import unittest

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

class TestValidatePassword(unittest.TestCase):
    def test_password_too_short(self):
        self.assertFalse(validate_password('abc12'))

    def test_password_no_alpha(self):
        self.assertFalse(validate_password('123456'))

    def test_password_no_digit(self):
        self.assertFalse(validate_password('abcdef'))

    def test_password_ok(self):
        self.assertTrue(validate_password('abdef9'))
        self.assertTrue(validate_password('12345a'))

if __name__ == '__main__':
    unittest.main()