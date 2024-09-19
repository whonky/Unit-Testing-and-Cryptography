from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text
class TestConvertToText(TestCase):
    def test_convert_to_text_two_letters(self):
        self.assertEqual(convert_to_text(28, 2), "CB")

    def test_convert_to_text_two_letters_case_two(self):
        self.assertEqual(convert_to_text(53, 2), "BC")

    def test_convert_to_text_four_letters(self):
        self.assertEqual(convert_to_text(187253, 4), "BARK")

    def test_convert_to_text_thirty_six_letters(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977, 36), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

    def test_convert_to_text_zero(self):
        self.assertEqual(convert_to_text(0, 0), "")


