import os
import unittest
import lz78
from tiedosto_palvelu import TiedostoPalvelu


class TestLZ(unittest.TestCase):
    def test_lz_pakkaa(self):
        tiedosto = TiedostoPalvelu(os.path.join(os.getcwd(), 'data', 'simple_test.txt'))
        self.assertEqual(
            lz78.pakkaa(tiedosto.lue_tiedosto()),
            "0A1B2A0B0C4C4D7B3A1A5C1C0D5D14A10C13C13A2C16B12A10B5A7D5B"
        )
