from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode
class TestCaesarDecode(TestCase):
    def test_caesar_decode_lowercase_word(self):
        self.assertEqual(caesar_decode("jgnnq", 2), "hello")

    def test_caesar_decode_uppercase_word(self):
        self.assertEqual(caesar_decode("KHOOR", 3), "HELLO")

    def test_caesar_decode_upper_and_lowercase_word(self):
        self.assertEqual(caesar_decode("Lipps", 4), "Hello")

    def test_caesar_decode_end_letters(self):
        self.assertEqual(caesar_decode("ejgwf", 5), "zebra")

    def test_caesar_decode_numbers(self):
        self.assertEqual(caesar_decode("12", 5), "12")

    def test_caesar_encode_integers(self):
        self.assertEqual(caesar_decode(12, 5), "12")

    def test_caesar_encode_floats(self):
        self.assertEqual(caesar_decode(1.2, 5), "1.2")

    def test_caesar_encode_boolean(self):
        self.assertEqual(caesar_decode(True, 5), "Ompz")

    def test_caesar_decode_special_characters(self):
        self.assertEqual(caesar_decode("@#$%^&*()", 5), "@#$%^&*()")

    def test_caesar_decode_blank(self):
        self.assertEqual(caesar_decode("", 5), "")

    def test_caesar_decode_space(self):
        self.assertEqual(caesar_decode(" ", 5), " ")

    def test_caesar_decode_long_shift(self):
        self.assertEqual(caesar_decode("nkrru", 32), "hello")

    def test_caesar_decode_sentence(self):
        self.assertEqual(caesar_decode("Olssv, tf uhtl pz Ohuh.", 7), "Hello, my name is Hana.")





