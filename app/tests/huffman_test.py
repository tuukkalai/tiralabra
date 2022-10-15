import os
import unittest
import huffman


class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.testi_teksti = "AABABABBBCBCBBABABBBAB"

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

    def test_tiedoston_lukeminen(self):
        teksti = huffman.lue_tiedosto(
            os.path.join(os.getcwd(), "data", "simple_test.txt")
        )
        self.assertEqual(
            teksti, "AABABABCBCBDBDBABAAAACCACDCDCDAAACDCDAABCAACBACAAABCABDDCBABAA"
        )

    def test_testitiedoston_pakkaaminen(self):
        tiedosto = huffman.pakkaa(os.path.join(os.getcwd(), "data", "simple_test.txt"))
        self.assertEqual(
            tiedosto, os.path.join(os.getcwd(), "data", "simple_test.txt.huff")
        )
