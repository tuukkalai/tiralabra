import os
import unittest
import lz78
from tiedosto_palvelu import TiedostoPalvelu


class TestLZ(unittest.TestCase):
    def setUp(self) -> None:
        self.tiedosto = os.path.join(os.getcwd(), "data", "simple_test.txt")

    def test_lzpakkaa_tuottaa_pakatun_tiedoston(self):
        pakattu_tiedosto_sijainti = lz78.pakkaa(self.tiedosto)

        self.assertTrue(os.path.isfile(pakattu_tiedosto_sijainti))

    def test_lzpura_purkaa_pakatun_tiedoston_oikein(self):
        pakattu_tiedosto_sijainti = lz78.pakkaa(self.tiedosto)

        purettu_tiedosto_sijainti = lz78.pura(pakattu_tiedosto_sijainti)
        purettu_tiedosto_sisalto = TiedostoPalvelu(
            purettu_tiedosto_sijainti
        ).lue_tiedosto()

        self.assertEqual(
            TiedostoPalvelu(self.tiedosto).lue_tiedosto(), purettu_tiedosto_sisalto
        )

    def test_kayttoohje_nakyy_vivulla(self):
        tuloste = lz78.kayttoohje()
        self.assertEqual(
            """
    Tekstitiedoston pakkaaminen ja purkaminen LZ78-algoritmilla
    
    ┌──────────────────────────────────────────────────────────┐
    │  Käyttö:                                                 │
    │    poetry run python app/lz78.py [vipu] [tiedosto]       │
    └──────────────────────────────────────────────────────────┘
    
    Vivut:
      -c          pakkaa annettu tiedosto
      -d          pura annettu tiedosto
      -h          näytä ohje
    """,
            tuloste,
        )
