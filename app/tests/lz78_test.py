import os
import unittest
import lz78
from tiedosto_palvelu import TiedostoPalvelu


class TestLZ(unittest.TestCase):
    def setUp(self) -> None:
        self.tiedosto = TiedostoPalvelu(
            os.path.join(os.getcwd(), "data", "simple_test.txt")
        )

    def test_lzpakkaa_tuottaa_pakatun_tiedoston(self):
        pakattu_tiedosto = TiedostoPalvelu(str(self.tiedosto))
        pakattu_tiedosto.kirjoita_tiedosto(
            lz78.pakkaa(self.tiedosto.lue_tiedosto()), "w+b"
        )
        self.assertTrue(os.path.isfile(str(pakattu_tiedosto)))

    def test_lzpura_purkaa_pakatun_tiedoston_oikein(self):
        pakattu_tiedosto = TiedostoPalvelu(str(self.tiedosto))
        pakattu_tiedosto = pakattu_tiedosto.kirjoita_tiedosto(
            lz78.pakkaa(self.tiedosto.lue_tiedosto()), "w+b"
        )
        tiedosto = TiedostoPalvelu(str(pakattu_tiedosto))
        pakattu_tiedosto_sisalto = tiedosto.lue_tiedosto()
        purettu_tiedosto_sijainti = tiedosto.kirjoita_tiedosto(
            lz78.pura(pakattu_tiedosto_sisalto), "w"
        )
        purettu_tiedosto = TiedostoPalvelu(purettu_tiedosto_sijainti)
        self.assertEqual(self.tiedosto.lue_tiedosto(), purettu_tiedosto.lue_tiedosto())

    def test_kayttoohje_nakyy_vivulla(self):
        tuloste = lz78.kayttoohje()
        self.assertEqual(
            """
    Tekstitiedoston pakkaaminen ja purkaminen LZ78-algoritmilla
    
    ┌──────────────────────────────────────────────────────────┐
    │  Käyttö:                                                 │
    │    poetry run invoke lzpakkaa [tiedosto]                 │
    │    poetry run invoke lzpura [tiedosto]                   │
    └──────────────────────────────────────────────────────────┘
    
    Sovelluksen voi käynnistää myös ilman poetryn komentoja:
      python3 app/lz78.py [vipu] [tiedosto]
    
    Vivut:
      -c          pakkaa annettu tiedosto
      -d          pura annettu tiedosto
      -h          näytä ohje
    """,
            tuloste,
        )
