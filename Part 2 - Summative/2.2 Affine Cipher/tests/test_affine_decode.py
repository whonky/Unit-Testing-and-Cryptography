from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode
class TestAffineDecode(TestCase):
    def test_affine_decode_lowercase_text(self):
        self.assertEqual(affine_decode("armmv", 3, 5), "hello")

    def test_affine_decode_uppercase_text(self):
        self.assertEqual(affine_decode("ARMMV", 3, 5), "HELLO")

    def test_affine_decode_uppercase_and_lowercase_text(self):
        self.assertEqual(affine_decode("Armmv", 3, 5), "Hello")

    def test_affine_decode_blank(self):
        self.assertEqual(affine_decode("", 3, 5), "")

    def test_affine_decode_space(self):
        self.assertEqual(affine_decode(" ", 3, 5), " ")

    def test_affine_decode_special_chars(self):
        self.assertEqual(affine_decode("!@#$%^&*()", 3, 5), "!@#$%^&*()")

    def test_affine_decode_numbers(self):
        self.assertEqual(affine_decode("1234567890", 3, 5), "1234567890")

    def test_affine_decode_sentence(self):
        self.assertEqual(affine_decode("Hmjje, qw xkqm og Hkxk! O kq ox 12nh azkfm.", 7, 10), "Hello, my name is Hana! I am in 12th grade.")

    def test_affine_decode_long_shift(self):
        self.assertEqual(affine_decode("zqllu", 3, 30), "hello")

    def test_affine_decode_small_shift(self):
        self.assertEqual(affine_decode("wniir", 3, 1), "hello")


