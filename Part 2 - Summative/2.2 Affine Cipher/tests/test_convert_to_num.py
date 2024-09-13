from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num
class TestConvertToNum(TestCase):
    def test_convert_to_num_lowercase_text(self):
        self.assertEqual(convert_to_num("DE"), )

