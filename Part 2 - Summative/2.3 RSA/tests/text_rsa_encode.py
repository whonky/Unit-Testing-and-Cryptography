from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import rsa_encode
class TestRsaEncode(TestCase):
    def test_rsa_encode(self):
        self.assertEqual(rsa_encode("THEFIVEBOXINGWIZARDSJUMPQUICKLY",
                                    292361466231755597564095925310764764819 * 307125506157764866722739041634199200019,
                                    65537),
                         34028226424022141662679340496616735128390579906964150145035108807466384852365)
