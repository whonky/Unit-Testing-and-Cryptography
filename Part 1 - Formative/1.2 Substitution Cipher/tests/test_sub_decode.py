from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode
class TestSubDecode(TestCase):
    def test_sub_decode_lowercase_word_and_codebet(self):
        self.assertEqual(sub_decode("mxtth", "WJKUXVBMIYDTPLHZGONCRSAEFQ".lower()), "hello")

    def test_sub_decode_uppercase_word_and_codebet(self):
        self.assertEqual(sub_decode("MXTTH", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLO")

    def test_sub_decode_uppercase_word_lowercase_codebet(self):
        self.assertEqual(sub_decode("YWBBF", "scxawklytzuboifvhmrepqgdjn"), "HELLO")

    def test_sub_decode_lowercase_word_uppercase_codebet(self):
        self.assertEqual(sub_decode("ywbbf", "scxawklytzuboifvhmrepqgdjn".upper()), "hello")

    def test_sub_decode_lowercase_and_uppercase_word_lowercase_codebet(self):
        self.assertEqual(sub_decode("Jtlls", "koxvtewjfzblmysrcqhandgpiu"), "Hello")

    def test_sub_decode_lowercase_and_uppercase_word_uppercase_codebet(self):
        self.assertEqual(sub_decode("Jtlls", "koxvtewjfzblmysrcqhandgpiu".upper()), "Hello")

    def test_sub_decode_special_characters(self):
        self.assertEqual(sub_decode("!@#$%^&*()", "koxvtewjfzblmysrcqhandgpiu"), "!@#$%^&*()")

    def test_sub_decode_numbers(self):
        self.assertEqual(sub_decode("1234567890", "koxvtewjfzblmysrcqhandgpiu"), "1234567890")

    def test_sub_decode_blank(self):
        self.assertEqual(sub_decode("", "koxvtewjfzblmysrcqhandgpiu"), "")

    def test_sub_decode_space(self):
        self.assertEqual(sub_decode(" ", "koxvtewjfzblmysrcqhandgpiu"), " ")

    def test_sub_decode_sentence(self):
        self.assertEqual(sub_decode("Jtlls, mi ykmt fh Jkyk.", "koxvtewjfzblmysrcqhandgpiu"), "Hello, my name is Hana.")

    def test_sub_decode_integers(self):
        self.assertEqual(sub_decode(1234567890, "koxvtewjfzblmysrcqhandgpiu"), "1234567890")

    def test_sub_decode_floats(self):
        self.assertEqual(sub_decode(1.2, "koxvtewjfzblmysrcqhandgpiu"), "1.2")

    def test_sub_decode_boolean(self):
        self.assertEqual(sub_decode(True, "koxvtewjfzblmysrcqhandgpiu"), "Epzf")

    def test_sub_decode_codebet_with_special_chars(self):
        self.assertEqual(sub_decode("=.zm=", "=JKUXVBMIYD.PLHZGONCRSAEFQ".lower()), "alpha")

    def test_sub_decode_codebet_with_numbers(self):
        self.assertEqual(sub_decode("12zm1", "1JKUXVBMIYD2PLHZGONCRSAEFQ".lower()), "alpha")