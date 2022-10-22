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

    def test_olematon_tiedosto_palauttaa_varauksen_tiedostoon(self):
        tiedosto = TiedostoPalvelu(os.path.join("data", "olematon_tiedosto.txt"))
        self.assertEqual(str(tiedosto), os.path.join("data", "olematon_tiedosto.txt"))

    def test_olemattoman_tiedoston_lukeminen_palauttaa_virheen(self):
        with self.assertRaises(OSError):
            tiedoston_sisalto = TiedostoPalvelu(
                os.path.join("data", "olematon_tiedosto.txt")
            ).lue_tiedosto()
