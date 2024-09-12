from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode
class TestAffineEncode(TestCase):
    def test_affine_encode_lowercase_text(self):
        self.assertEqual(affine_encode("hello", 3, 5), "armmv")

    def test_affine_encode_uppercase_text(self):
        self.assertEqual(affine_encode("HELLO", 3, 5), "ARMMV")

    def test_affine_encode_uppercase_and_lowercase_text(self):
        self.assertEqual(affine_encode("Hello", 3, 5), "Armmv")

    def test_affine_encode_blank(self):
        self.assertEqual(affine_encode("", 3, 5), "")

    def test_affine_encode_space(self):
        self.assertEqual(affine_encode(" ", 3, 5), " ")

    def test_affine_encode_special_chars(self):
        self.assertEqual(affine_encode("!@#$%^&*()", 3, 5), "!@#$%^&*()")

    def test_affine_encode_numbers(self):
        self.assertEqual(affine_encode("1234567890", 3, 5), "1234567890")

    def test_affine_encode_sentence(self):
        self.assertEqual(affine_encode("Hello, my name is Hana! I am in 12th grade.", 7, 10), "Hmjje, qw xkqm og Hkxk! O kq ox 12nh azkfm.")

    def test_affine_encode_long_shift(self):
        self.assertEqual(affine_encode("hello", 3, 30), "zqllu")

    def test_affine_encode_small_shift(self):
        self.assertEqual(affine_encode("hello", 3, 1), "kveet")


