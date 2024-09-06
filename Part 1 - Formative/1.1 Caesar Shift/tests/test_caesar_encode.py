from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode
class TestCaesarEncode(TestCase):
    def test_caesar_encode_lowercase_word(self):
        self.assertEqual(caesar_encode("hello", 2), "jgnnq")

    def test_caesar_encode_uppercase_word(self):
        self.assertEqual(caesar_encode("HELLO", 3), "KHOOR")

    def test_caesar_encode_upper_and_lowercase_word(self):
        self.assertEqual(caesar_encode("Hello", 4), "Lipps")

    def test_caesar_encode_end_letters(self):
        self.assertEqual(caesar_encode("zebra", 5), "ejgwf")

    def test_caesar_encode_numbers(self):
        self.assertEqual(caesar_encode("12", 5), "12")

    def test_caesar_encode_special_characters(self):
        self.assertEqual(caesar_encode("@#$%^&*()", 5), "@#$%^&*()")

    def test_caesar_encode_blank(self):
        self.assertEqual(caesar_encode("", 5), "")

    def test_caesar_encode_space(self):
        self.assertEqual(caesar_encode(" ", 5), " ")

    def test_caesar_encode_long_shift(self):
        self.assertEqual(caesar_encode("hello", 32), "nkrru")

    def test_caesar_encode_sentence(self):
        self.assertEqual(caesar_encode("Hello, my name is Hana.", 7), "Olssv, tf uhtl pz Ohuh.")





