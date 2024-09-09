from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode
class TestVigEncode(TestCase):
    def test_vig_encode_lowercase_text_and_keyword(self):
        self.assertEqual(vig_encode("hello", "test"), "aideh")

    def test_vig_encode_uppercase_text_and_keyword(self):
        self.assertEqual(vig_encode("hello".upper(), "test".upper()), "aideh".upper())

    def test_vig_encode_lowercase_text_uppercase_keyword(self):
        self.assertEqual(vig_encode("hello", "test".upper()), "aideh")

    def test_vig_encode_uppercase_text_lowercase_keyword(self):
        self.assertEqual(vig_encode("hello".upper(), "test"), "aideh".upper())

    def test_vig_encode_numbers(self):
        self.assertEqual(vig_encode("123", "encode"), "aideh".upper())





