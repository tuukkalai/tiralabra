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

    def pakkaa_ja_pura_tiedosto(self, tiedosto: str) -> tuple:
        testi_tiedosto = os.path.join(os.getcwd(), "data", tiedosto)
        pakattu_tiedosto_nimi = lz78.pakkaa(testi_tiedosto)

        purettu_tiedosto_nimi = lz78.pura(pakattu_tiedosto_nimi)
        purettu_tiedosto_sisalto = TiedostoPalvelu(purettu_tiedosto_nimi).lue_tiedosto()

        alkuperainen_sisalto = TiedostoPalvelu(testi_tiedosto).lue_tiedosto()

        return (alkuperainen_sisalto, purettu_tiedosto_sisalto)

    def test_purettu_tiedosto_vastaa_alkuperaista_yksinkertainen(self):
        (alkuperainen_sisalto, purettu_sisalto) = self.pakkaa_ja_pura_tiedosto(
            "simple_test.txt"
        )
        self.assertEqual(alkuperainen_sisalto, purettu_sisalto)

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
