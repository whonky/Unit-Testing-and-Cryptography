from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode
class TestVigEncode(TestCase):
    def test_vig_encode_lowercase_text_and_keyword(self):
        self.assertEqual(vig_encode("hello", "test"), "_ICDG")

    def test_vig_encode_uppercase_text_and_keyword(self):
        self.assertEqual(vig_encode("hello".upper(), "test".upper()), "_ICDG")

    def test_vig_encode_lowercase_text_uppercase_keyword(self):
        self.assertEqual(vig_encode("hello", "test".upper()), "_ICDG")

    def test_vig_encode_uppercase_text_lowercase_keyword(self):
        self.assertEqual(vig_encode("hello".upper(), "test"), "_ICDG")

    def test_vig_encode_uppercase_and_lowercase_keyword(self):
        self.assertEqual(vig_encode("hello", "Test"), "_ICDG")

    def test_vig_encode_uppercase_and_lowercase_text(self):
        self.assertEqual(vig_encode("heLlo", "test"), "_ICDG")

    def test_vig_encode_long_keyword(self):
        self.assertEqual(vig_encode("hello", "pneumonoultramicroscopicsilicovolcanoconiosis"), "WRPE_")

    def test_vig_encode_one_letter_keyword(self):
        self.assertEqual(vig_encode("hello", "h"), "OLSSV")

    def test_vig_encode_number_in_keyword(self):
        self.assertEqual(vig_encode("hello", "1test2test"), "_ICDG")

    def test_vig_encode_special_chars_in_keyword(self):
        self.assertEqual(vig_encode("hello", "!test?test"), "_ICDG")

    def test_vig_encode_numbers(self):
        self.assertEqual(vig_encode("123", "encode"), "")

    def test_vig_encode_special_chars(self):
        self.assertEqual(vig_encode("!@#$%^&*()", "encode"), "")

    def test_vig_encode_blank(self):
        self.assertEqual(vig_encode("", "encode"), "")

    def test_vig_encode_space(self):
        self.assertEqual(vig_encode(" ", "encode"), "D")

    def test_vig_encode_sentence(self):
        self.assertEqual(vig_encode("Hello, my name is Hana! I am in 12th grade.", "encode"), "LRNZRDQKBADQIMKFCLE_CNLDEZBWQDXUBUUEHR")





