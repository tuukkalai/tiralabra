import unittest
import huffman

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.testi_teksti = 'AABABABBBCBCBBABABBBAB'

    def test_esiintyvyyslaskin_palauttaa_listan_tupleja(self):
        sanakirja = huffman.esiintyvyys_laskin(self.testi_teksti)
        self.assertEqual(type(sanakirja), list)
        self.assertEqual(type(sanakirja[0]), tuple)
