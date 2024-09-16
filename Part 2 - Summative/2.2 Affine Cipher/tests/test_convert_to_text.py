from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text
class TestConvertToText(TestCase):
    def test_convert_to_text_two_letters(self):
        self.assertEqual(convert_to_text(28), "CB")

    def test_convert_to_text_two_letters_case_two(self):
        self.assertEqual(convert_to_text(53), "BC")

    def test_convert_to_text_four_letters(self):
        self.assertEqual(convert_to_text(187253), "BARK")

    def test_convert_to_text_thirty_five_letters(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

    def test_convert_to_text_zero(self):
        self.assertEqual(convert_to_text(0), "")


