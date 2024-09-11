from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode
class TestVigDecode(TestCase):
    def test_vig_decode_lowercase_text_and_keyword(self):
        self.assertEqual(vig_decode(" icdg", "test"), "HELLO")

    def test_vig_decode_uppercase_text_and_keyword(self):
        self.assertEqual(vig_decode(" ICDG".upper(), "test".upper()), "HELLO")

    def test_vig_decode_lowercase_text_uppercase_keyword(self):
        self.assertEqual(vig_decode("_icdg", "test".upper()), "HELLO")

    def test_vig_decode_uppercase_text_lowercase_keyword(self):
        self.assertEqual(vig_decode("_ICDG", "test"), "HELLO")

    def test_vig_decode_uppercase_and_lowercase_keyword(self):
        self.assertEqual(vig_decode("_ICDG", "Test"), "HELLO")

    def test_vig_decode_uppercase_and_lowercase_text(self):
        self.assertEqual(vig_decode("_iCdg", "test"), "HELLO")

    def test_vig_decode_long_keyword(self):
        self.assertEqual(vig_decode("WRPE_", "pneumonoultramicroscopicsilicovolcanoconiosis"), "HELLO")

    def test_vig_decode_one_letter_keyword(self):
        self.assertEqual(vig_decode("OLSSV", "h"), "HELLO")

    def test_vig_decode_number_in_keyword(self):
        self.assertEqual(vig_decode("_ICDG", "1test2test"), "HELLO")

    def test_vig_decode_special_chars_in_keyword(self):
        self.assertEqual(vig_decode("_ICDG", "!test?test"), "HELLO")

    def test_vig_decode_numbers(self):
        self.assertEqual(vig_decode("123", "decode"), "")

    def test_vig_decode_special_chars(self):
        self.assertEqual(vig_decode("!@#$%^&*()", "decode"), "")

    def test_vig_decode_blank(self):
        self.assertEqual(vig_decode("", "decode"), "")

    def test_vig_decode_space(self):
        self.assertEqual(vig_decode(" ", "decode"), "X")

    def test_vig_decode_sentence(self):
        self.assertEqual(vig_decode("Hello, my name is Hana! I am in 12th grade.", "decode"), "EAJYLWJUY_YIBWGEXDYJZMFWYIYVKWQDYTOXAA")





