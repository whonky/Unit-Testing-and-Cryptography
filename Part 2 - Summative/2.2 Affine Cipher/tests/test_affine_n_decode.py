from unittest import TestCase
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode


class TestAffineNDecode(TestCase):
    def test_affine_n_decode_uppercase_text_and_evenly_divisible_n(self):
        self.assertEqual(affine_n_decode("XUHN", 2, 3, 121), "COOL")

    def test_affine_n_decode_uppercase_text_and_non_evenly_divisible_n(self):
        self.assertEqual(affine_n_decode("XURYWT", 3, 3, 121), "COOLXX")

    def test_affine_n_decode_lowercase_text_and_evenly_divisible_n(self):
        self.assertEqual(affine_n_decode("xuhn", 2, 3, 121), "COOL")

    def test_affine_n_decode_lowercase_text_and_non_evenly_divisible_n(self):
        self.assertEqual(affine_n_decode("xurywt", 3, 3, 121), "COOLXX")

    def test_affine_n_decode_lowercase_and_uppercase_text(self):
        self.assertEqual(affine_n_decode("xURYWT", 3, 3, 121), "COOLXX")

    def test_affine_n_decode_special_character_in_text(self):
        self.assertEqual(affine_n_decode("?XUHN", 2, 3, 121), "COOL")

    def test_affine_n_decode_space_in_text(self):
        self.assertEqual(affine_n_decode(" XUHN", 2, 3, 121), "COOL")

    def test_affine_n_decode_number_in_text(self):
        self.assertEqual(affine_n_decode("XUHN1", 2, 3, 121), "COOL")

    def test_affine_n_decode_long_text(self):
        self.assertEqual(affine_n_decode("USLTFZITNPBJEWREMCQTPQONLCWPJAFFGWWHPZFG", 5, 347, 1721),
                         "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGXXXX")

    def test_affine_n_decode_n_equals_one(self):
        self.assertEqual(affine_n_decode("UQPTDZXROCBVSYBEIDJKPGBMPCUQPAFWNGBH", 1, 347, 1721),
                         "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

    def test_affine_n_decode_n_equals_text_length(self):
        self.assertEqual(affine_n_decode("USLTFJFRNPPDCWRGFAQTIKMNLJKNJATWDWWI", 36, 347, 1721),
                         "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")

    def test_affine_n_decode_n_greater_than_text_length(self):
        self.assertEqual(affine_n_decode("USLTFJFRNPPDCWRGFAQTIKMNLJKNJATWDWWIIXFGGGGGGGGGGG", 50, 347, 1721),
                         "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGXXXXXXXXXXXXXX")