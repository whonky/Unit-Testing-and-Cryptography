from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num
class TestConvertToNum(TestCase):
    def test_convert_to_num_uppercase_text(self):
        self.assertEqual(convert_to_num("CB"), 28)

    def test_convert_to_num_lowercase_text(self):
        self.assertEqual(convert_to_num("cb"), 28)

    def test_convert_to_num_lowercase_and_uppercase_text(self):
        self.assertEqual(convert_to_num("Bc"), 53)

    def test_convert_to_num_four_letters(self):
        self.assertEqual(convert_to_num("BARK"), 187253)

    def test_convert_to_num_space(self):
        self.assertEqual(convert_to_num(" "), 0)

    def test_convert_to_num_blank(self):
        self.assertEqual(convert_to_num(""), 0)

    def test_convert_to_num_special_chars(self):
        self.assertEqual(convert_to_num("!@#$%^&*()"), 0)

    def test_convert_to_num_numbers(self):
        self.assertEqual(convert_to_num("1234567890"), 0)

    def test_convert_to_num_integrated_space(self):
        self.assertEqual(convert_to_num("B ARK"), 187253)

    def test_convert_to_num_integrated_special_char(self):
        self.assertEqual(convert_to_num("B*ARK"), 187253)

    def test_convert_to_num_integrated_number(self):
        self.assertEqual(convert_to_num("B1ARK"), 187253)

    def test_convert_to_num_long_text(self):
        self.assertEqual(convert_to_num("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"), 218741750267309021256255930435388550208768849997977)