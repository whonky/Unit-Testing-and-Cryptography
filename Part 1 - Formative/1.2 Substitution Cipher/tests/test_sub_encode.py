from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode
class TestSubEncode(TestCase):
    def test_sub_encode_lowercase_word_and_codebet(self):
        self.assertEqual(sub_encode("hello", "WJKUXVBMIYDTPLHZGONCRSAEFQ".lower()), "mxtth")

    def test_sub_encode_uppercase_word_and_codebet(self):
        self.assertEqual(sub_encode("HELLO", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTH")

    def test_sub_encode_uppercase_word_lowercase_codebet(self):
        self.assertEqual(sub_encode("HELLO", "scxawklytzuboifvhmrepqgdjn"), "YWBBF")

    def test_sub_encode_lowercase_word_uppercase_codebet(self):
        self.assertEqual(sub_encode("hello", "scxawklytzuboifvhmrepqgdjn".upper()), "ywbbf")

    def test_sub_encode_lowercase_and_uppercase_word_lowercase_codebet(self):
        self.assertEqual(sub_encode("Hello", "koxvtewjfzblmysrcqhandgpiu"), "Jtlls")

    def test_sub_encode_lowercase_and_uppercase_word_uppercase_codebet(self):
        self.assertEqual(sub_encode("Hello", "koxvtewjfzblmysrcqhandgpiu".upper()), "Jtlls")

    def test_sub_encode_special_characters(self):
        self.assertEqual(sub_encode("!@#$%^&*()", "koxvtewjfzblmysrcqhandgpiu"), "!@#$%^&*()")

    def test_sub_encode_numbers(self):
        self.assertEqual(sub_encode("1234567890", "koxvtewjfzblmysrcqhandgpiu"), "1234567890")

    def test_sub_encode_blank(self):
        self.assertEqual(sub_encode("", "koxvtewjfzblmysrcqhandgpiu"), "")

    def test_sub_encode_space(self):
        self.assertEqual(sub_encode(" ", "koxvtewjfzblmysrcqhandgpiu"), " ")

    def test_sub_encode_sentence(self):
        self.assertEqual(sub_encode("Hello, my name is Hana.", "koxvtewjfzblmysrcqhandgpiu"), "Jtlls, mi ykmt fh Jkyk.")

    def test_sub_encode_integers(self):
        self.assertEqual(sub_encode(1234567890, "koxvtewjfzblmysrcqhandgpiu"), "1234567890")

    def test_sub_encode_floats(self):
        self.assertEqual(sub_encode(1.2, "koxvtewjfzblmysrcqhandgpiu"), "1.2")

    def test_sub_encode_boolean(self):
        self.assertEqual(sub_encode(True, "koxvtewjfzblmysrcqhandgpiu"), "Aqnt")

    def test_sub_encode_codebet_with_special_chars(self):
        self.assertEqual(sub_encode("alpha", "=JKUXVBMIYD.PLHZGONCRSAEFQ".lower()), "=.zm=")

    def test_sub_encode_codebet_with_numbers(self):
        self.assertEqual(sub_encode("alpha", "1JKUXVBMIYD2PLHZGONCRSAEFQ".lower()), "12zm1")