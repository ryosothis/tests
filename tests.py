import unittest
import string
from testapp import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_password_generation(self):
        """Тест генерации пароля с параметрами по умолчанию"""
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(len(password) == 12)
    
    def test_password_length(self):
        """Тест различной длины пароля"""
        for length in [8, 12, 15]:
            password = generate_password(length=length)
            self.assertEqual(len(password), length)
    
    def test_password_without_special_chars(self):
        """Тест генерации без специальных символов"""
        password = generate_password(use_special_chars=False)
        for char in password:
            self.assertNotIn(char, string.punctuation)
    
    def test_invalid_input(self):
        """Тест обработки невалидных входных данных"""
        with self.assertRaises(ValueError):
            generate_password(length=0)
        with self.assertRaises(ValueError):
            generate_password(use_digits=False, use_special_chars=False)

if __name__ == '__main__':
    unittest.main()