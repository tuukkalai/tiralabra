import os
import unittest
from tiedosto_palvelu import TiedostoPalvelu


class TestTiedostoPalvelu(unittest.TestCase):
    def setUp(self):
        pass

    def test_relatiivinen_polku_palauttaa_tiedoston(self):
        tiedosto = TiedostoPalvelu(os.path.join("data", "simple_test.txt"))
        self.assertEqual(
            tiedosto.lue_tiedosto(),
            "AABABABCBCBDBDBABAAAACCACDCDCDAAACDCDAABCAACBACAAABCABDDCBABAA",
        )

    def test_eksakti_polku_palauttaa_tiedoston(self):
        tiedosto = TiedostoPalvelu(os.path.join(os.getcwd(), "data", "simple_test.txt"))
        self.assertEqual(
            tiedosto.lue_tiedosto(),
            "AABABABCBCBDBDBABAAAACCACDCDCDAAACDCDAABCAACBACAAABCABDDCBABAA",
        )

    def test_olematon_tiedosto_palauttaa_virheen(self):
        with self.assertRaises(OSError):
            TiedostoPalvelu(os.path.join("data", "olematon_tiedosto.txt"))
