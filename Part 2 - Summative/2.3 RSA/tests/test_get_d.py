from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import get_d
class TestGetD(TestCase):
    def test_get_d(self):
        self.assertEqual(get_d(2003, 2503, 17),2946473)
