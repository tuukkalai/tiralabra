import os
import unittest
import huffman
from tiedosto_palvelu import TiedostoPalvelu


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.testi_teksti = "AABABABBBCBCBBABABBBAB"
        self.testi_tiedosto = os.path.join(os.getcwd(), "data", "simple_test.txt")

    def test_esiintyvyyslaskin_palauttaa_listan_tupleja(self):
        sanakirja = huffman.esiintyvyys_laskin(self.testi_teksti)
        self.assertEqual(type(sanakirja), list)
        self.assertEqual(type(sanakirja[0]), tuple)

    def test_esiintyvyyslaskin_palauttaa_oikean_maaran_kirjaimia(self):
        sanakirja = huffman.esiintyvyys_laskin(self.testi_teksti)
        self.assertEqual(len(sanakirja), 3)

    def test_esiintyvyyslaskin_palauttaa_kirjainten_maaran_oikein(self):
        sanakirja = huffman.esiintyvyys_laskin(self.testi_teksti)
        self.assertEqual(sanakirja[0][1], 13)
        self.assertEqual(sanakirja[1][1], 7)
        self.assertEqual(sanakirja[2][1], 2)

    def test_esiintyvyyslaskin_palauttaa_kirjaimet_oikeassa_jarjestyksessa(self):
        sanakirja = huffman.esiintyvyys_laskin(self.testi_teksti)
        self.assertGreater(sanakirja[0][1], sanakirja[1][1])
        self.assertGreater(sanakirja[1][1], sanakirja[2][1])

    def test_huffman_puu_palauttaa_sanakirjan(self):
        sanakirja = huffman.esiintyvyys_laskin(self.testi_teksti)
        bitti_koodi_sanakirja = huffman.huffman_puu(sanakirja)
        self.assertEqual(type(bitti_koodi_sanakirja), dict)

    def test_huffman_puu_palauttaa_oikean_lasketun_binaari_arvon_kirjaimelle(self):
        sanakirja = huffman.esiintyvyys_laskin(self.testi_teksti)
        bitti_koodi_sanakirja = huffman.huffman_puu(sanakirja)
        self.assertEqual(bitti_koodi_sanakirja["A"], "01")

    def test_huffman_binaari_palauttaa_sanakirjan(self):
        juuri = (("A", "B"), ("C", "D"))
        binaari = huffman.huffman_binaari(juuri)
        self.assertEqual(type(binaari), dict)

    def test_huffman_binaari_palauttaa_merkin_ja_binaariarvon_jos_ollaan_lehdessa(self):
        binaari = huffman.huffman_binaari("A", "001")
        self.assertEqual(binaari, {"A": "001"})

    def test_testitiedoston_pakkaaminen_tuottaa_pakatun_tiedoston(self):
        pakattu_tiedosto = huffman.pakkaa(self.testi_tiedosto)

        self.assertEqual(
            pakattu_tiedosto, os.path.join(os.getcwd(), "data", "simple_test.txt.huff")
        )

    def test_testitiedoston_purkaminen_tuottaa_puretun_tiedoston(self):
        # Pakataan testitiedosto
        pakattu_tiedosto_nimi = huffman.pakkaa(self.testi_tiedosto)

        # Puretaan testitiedosto
        purettu_tiedosto_nimi = huffman.pura(pakattu_tiedosto_nimi)

        self.assertEqual(
            purettu_tiedosto_nimi,
            os.path.join(os.getcwd(), "data", "simple_test.txt.huff.purettu"),
        )

    def pakkaa_ja_pura_tiedosto(self, tiedosto: str) -> tuple:
        testi_tiedosto = os.path.join(os.getcwd(), "data", tiedosto)
        pakattu_tiedosto_nimi = huffman.pakkaa(testi_tiedosto)

        purettu_tiedosto_nimi = huffman.pura(pakattu_tiedosto_nimi)
        purettu_tiedosto_sisalto = TiedostoPalvelu(purettu_tiedosto_nimi).lue_tiedosto()

        alkuperainen_sisalto = TiedostoPalvelu(testi_tiedosto).lue_tiedosto()

        return (alkuperainen_sisalto, purettu_tiedosto_sisalto)

    # def test_purettu_tiedosto_vastaa_alkuperaista_yksinkertainen(self):
    #     (alkuperainen_sisalto, purettu_sisalto) = self.pakkaa_ja_pura_tiedosto(
    #         "simple_test.txt"
    #     )
    #     self.assertEqual(alkuperainen_sisalto, purettu_sisalto)

    # def test_purettu_tiedosto_vastaa_alkuperaista_koodi(self):
    #     (alkuperainen_sisalto, purettu_sisalto) = self.pakkaa_ja_pura_tiedosto(
    #         "canterbury_corpus/fields.c"
    #     )
    #     self.assertEqual(alkuperainen_sisalto, purettu_sisalto)

    # def test_purettu_tiedosto_vastaa_alkuperaista_laulun_sanat(self):
    #     (alkuperainen_sisalto, purettu_sisalto) = self.pakkaa_ja_pura_tiedosto(
    #         "sia_cheap_thrills.txt"
    #     )
    #     self.assertEqual(alkuperainen_sisalto, purettu_sisalto)

    # def test_purettu_tiedosto_vastaa_alkuperaista_jfk(self):
    #     (alkuperainen_sisalto, purettu_sisalto) = self.pakkaa_ja_pura_tiedosto(
    #         "jfk_virkaanastujaispuhe.txt"
    #     )
    #     self.assertEqual(alkuperainen_sisalto, purettu_sisalto)

    # def test_aina_toimii(self):
    #     self.assertTrue(1 == 1)

    def test_kayttoohje_nakyy_vivulla(self):
        tuloste = huffman.kayttoohje()
        self.assertEqual(
            """
    Tekstitiedoston pakkaaminen ja purkaminen Huffman-algoritmilla
    
    ┌─────────────────────────────────────────────────────────────┐
    │  Käyttö:                                                    │
    │    poetry run invoke huffmanpakkaa --tiedosto=[tiedosto]    │
    │    poetry run invoke huffmanpura --tiedosto=[tiedosto]      │
    │    poetry run python app/huffman.py [vipu] [tiedosto]       │
    └─────────────────────────────────────────────────────────────┘
    
    Vivut:
      -c          pakkaa annettu tiedosto
      -d          pura annettu tiedosto
      -h          näytä ohje
    """,
            tuloste,
        )
