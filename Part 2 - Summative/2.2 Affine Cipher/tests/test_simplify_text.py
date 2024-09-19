from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import simplify_text


class TestSimplifyText(TestCase):
    def test_simplify_text_upper_and_lowercase(self):
        self.assertEqual(simplify_text("Hello"), "HELLO")

    def test_simplify_text_all_lowercase(self):
        self.assertEqual(simplify_text("hello"), "HELLO")

    def test_simplify_text_all_uppercase(self):
        self.assertEqual(simplify_text("HELLO"), "HELLO")

    def test_simplify_text_number(self):
        self.assertEqual(simplify_text("1Hello"), "HELLO")

    def test_simplify_text_space(self):
        self.assertEqual(simplify_text(" Hello"), "HELLO")
    def test_simplify_text_special_characters(self):
        self.assertEqual(simplify_text("!@#$%Hello"), "HELLO")
