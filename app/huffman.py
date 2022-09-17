import os
import sys


def esiintyvyys_laskin(syote: str) -> list:
    """Esiintyvyys laskin palauttaa listan tupleja syötteen kirjaimista järjestettynä esiintymistiheydeltään suurimmasta pienimpään.

    Args:
        syote (str): Pakattava syöte

    Returns:
        dict: Arvojen mukaan suurimmasta pienimpään järjestetty lista
    """
    sanakirja = {}

    for i in list(syote):
        if i in sanakirja:
            sanakirja[i] += 1
        else:
            sanakirja[i] = 1
    return sorted(sanakirja.items(), key=lambda item: item[1], reverse=True)


def huffman_binaari(solmu, binaari="") -> dict:
    """Binaarin muodostus aloitetaan saadusta Huffman puun solmusta. Tämän jälkeen puussa liikutaan seuraavalle tasolle kohti lehtiä, lisäten puun vasemmanpuoleisten haarojen solmujen binääriin luku 0, ja oikeanpuoleisten haarojen solmujen binääriin luku 1.

    Args:
        solmu (tuple tai str): Annetun solmun merkki/merkit ja merkin/merkkien arvo (lukumäärä tekstissä).
        binaari (str, optional): Solmun Huffman binäärimuotoinen esitys huffman_puu funktion kutsuhetkellä. Oletuksena saa arvon''.

    Returns:
        dict: Palauttaa sanakirjana merkit ja niitä vastaavat Huffman koodin antamat binäärimuotoiset esitykset.
    """
    if type(solmu) is str:
        return {solmu: binaari}
    (v, o) = (solmu[0], solmu[1])
    taulukko = dict()
    taulukko.update(huffman_binaari(v, binaari + "0"))
    taulukko.update(huffman_binaari(o, binaari + "1"))
    return taulukko


def huffman_puu(solmut: dict):
    while len(solmut) > 1:
        (merkki1, esiintyvyys1) = solmut[-1]
        (merkki2, esiintyvyys2) = solmut[-2]
        solmut = solmut[:-2]
        solmu = (merkki1, merkki2)
        solmut.append((solmu, esiintyvyys1 + esiintyvyys2))
        solmut = sorted(solmut, key=lambda x: x[1], reverse=True)
    return huffman_binaari(solmut[0][0])


def lue_tiedosto(tiedosto_nimi: str) -> None:
    """Lue annettu tiedosto.

    Args:
        tiedosto_nimi (str): Käsiteltävän tiedoston nimi.

    Returns:
        str: Palauttaa käsiteltävän tekstin tekstimuodossa.
    """
    with open(tiedosto_nimi) as tiedosto:
        teksti = tiedosto.read()
    return teksti


def pakkaa(tiedosto_nimi: str) -> dict:
    """Pää pakkausohjelma. Lukee annetun tiedoston, laskee käytettyjen merkkien määrät, muodostaa huffman_puun avulla merkkien ja binäärikoodien sanakirjan. Tulostaa ja palauttaa sanakirjan.

    Args:
        tiedosto_nimi (str): Käsiteltävän tiedoston nimi.
    """
    teksti = lue_tiedosto(tiedosto_nimi)
    merkit = esiintyvyys_laskin(teksti)
    solmut = merkit
    bitti_koodi_sanakirja = huffman_puu(solmut)

    for merkki in merkit:
        print(f"{repr(merkki[0]):4} -> {bitti_koodi_sanakirja[merkki[0]]}")

    return merkit


def main():
    pakattava_tiedosto = os.path.join(
        os.path.dirname(__file__), "tests", "jfk_virkaanastujaispuhe.txt"
    )
    if len(sys.argv) > 1:
        pakattava_tiedosto = os.path.join(os.getcwd(), sys.argv[1])
    pakkaa(pakattava_tiedosto)


if __name__ == "__main__":
    main()
