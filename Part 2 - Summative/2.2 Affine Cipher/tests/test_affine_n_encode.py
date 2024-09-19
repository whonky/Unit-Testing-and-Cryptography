from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_encode


class TestAffineNEncode(TestCase):
    def test_affine_n_encode_uppercase_text_and_evenly_divisible_n(self):
        self.assertEqual(affine_n_encode("COOL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_uppercase_text_and_non_evenly_divisible_n(self):
        self.assertEqual(affine_n_encode("COOL", 3, 3, 121), "XURYWT")

    def test_affine_n_encode_lowercase_text_and_evenly_divisible_n(self):
        self.assertEqual(affine_n_encode("cool", 2, 3, 121), "XUHN")

    def test_affine_n_encode_lowercase_text_and_non_evenly_divisible_n(self):
        self.assertEqual(affine_n_encode("cool", 3, 3, 121), "XURYWT")

    def test_affine_n_encode_lowercase_and_uppercase_text(self):
        self.assertEqual(affine_n_encode("Cool", 3, 3, 121), "XURYWT")

    def test_affine_n_encode_special_character_in_text(self):
        self.assertEqual(affine_n_encode("?COOL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_space_in_text(self):
        self.assertEqual(affine_n_encode(" COOL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_number_in_text(self):
        self.assertEqual(affine_n_encode("1COOL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_long_text(self):
        self.assertEqual(affine_n_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", 5, 347, 1721), "USLTFZITNPBJEWREMCQTPQONLCWPJAFFGWWHPZFG")

    def test_affine_n_encode_n_equals_one(self):
        self.assertEqual(affine_n_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", 1, 347, 1721),"UQPTDZXROCBVSYBEIDJKPGBMPCUQPAFWNGBH")

    def test_affine_n_encode_n_equals_text_length(self):
        self.assertEqual(affine_n_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", 36, 347, 1721),"USLTFJFRNPPDCWRGFAQTIKMNLJKNJATWDWWI")

    def test_affine_n_encode_n_greater_than_text_length(self):
        self.assertEqual(affine_n_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", 50, 347, 1721),"USLTFJFRNPPDCWRGFAQTIKMNLJKNJATWDWWIIXFGGGGGGGGGGG")