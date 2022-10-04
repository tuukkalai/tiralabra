import os
import sys


# Globaali muuttuja, johon kirjoitetaan pakatun tiedoston data
koodattava_teksti = ""


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
    Pakattavan tekstin merkkien binäärisanakirjaa muodostettaessa luodaan samalla postorder traversal algoritmia noudattaen Huffman puun esitys pakattavaan tiedostoon tallennettavaksi, muuttujaan `koodattava_teksti`.

    Args:
        solmu (tuple tai str): Annetun solmun merkki/merkit ja merkin/merkkien arvo (lukumäärä tekstissä).
        binaari (str, optional): Solmun Huffman binäärimuotoinen esitys huffman_puu funktion kutsuhetkellä. Oletuksena saa arvon''.

    Returns:
        dict: Palauttaa sanakirjana merkit ja niitä vastaavat Huffman koodin antamat binäärimuotoiset esitykset.
    """
    global koodattava_teksti

    if type(solmu) is str:
        koodattava_teksti += "1"
        koodattava_teksti += format(ord(solmu), "08b")
        return {solmu: binaari}
    (v, o) = (solmu[0], solmu[1])
    taulukko = dict()
    koodattava_teksti += "0"
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


def yhdista_sanakirja_ja_teksti(teksti: str, sanakirja: dict) -> None:
    """Lisätään globaalin muuttujan (koodattava_teksti) alkuun info (3-bit) kuinka monta nollaa poistetaan sanakirjan lopusta. Sanakirja (Huffman puu) osuuden loppuun lisätään nollia niin, että tulee 8-bittiä nollia -> sanakirja loppuu ja pakattu teksti alkaa.
    otsake = 3-bittiä,
    sanakirja = tarvittava määrä tavuja, lopussa otsakkeen merkitsemä määrä nollia
    erottaja = tavullinen nollia
    pakattu_teksti = sanakirjan avulla koottu pakattava teksti
    """
    global koodattava_teksti

    pakattu_teksti = ''
    for c in teksti:
        pakattu_teksti += sanakirja[c]

    tyhjaa = 8 - (len(koodattava_teksti) + len(pakattu_teksti)) % 8

    koodattava_teksti = format(tyhjaa, '08b') + koodattava_teksti + '0'*tyhjaa + '0'*8 + pakattu_teksti

def lisaa_pakattu_teksti(teksti: str, sanakirja: dict) -> None:
    global koodattava_teksti
    for c in teksti:
        koodattava_teksti += sanakirja[c]


def printtaa_koodattava_teksti() -> str:
    return koodattava_teksti


def pakkaa(tiedosto_nimi: str) -> None:
    """Pää pakkausohjelma. Lukee annetun tiedoston, laskee käytettyjen merkkien määrät, muodostaa huffman_puun avulla merkkien ja binäärikoodien sanakirjan. Tulostaa ja palauttaa sanakirjan.

    Args:
        tiedosto_nimi (str): Käsiteltävän tiedoston nimi.
    """

    teksti = lue_tiedosto(tiedosto_nimi)
    merkit = esiintyvyys_laskin(teksti)
    solmut = merkit
    bitti_koodi_sanakirja = huffman_puu(solmut)

    yhdista_sanakirja_ja_teksti(teksti, bitti_koodi_sanakirja)

    int_arr = []
    for b in range(0, len(koodattava_teksti), 8):
        int_arr.append(int(koodattava_teksti[b:b+8], 2))

    pakattu_tiedosto = tiedosto_nimi + '.huff'
    with open(pakattu_tiedosto, 'wb') as tiedosto:
        tiedosto.write(bytearray(int_arr))
    
    print(f'Pakattu tiedosto {pakattu_tiedosto} luotu.')


def pura(tiedosto_nimi: str) -> str:

    with open(tiedosto_nimi, 'rb') as tiedosto:
        teksti = tiedosto.read()
    
    nollia_lopussa = teksti[0]
    teksti = teksti[1:]

    binaari_teksti = ''
    for tavu in teksti:
        binaari_teksti += format(tavu, '08b')
    
    sanakirja = {}
    apumuuttuja = ''
    vali = ''
    bitti = 0

    pakattu_binaari = ''

    while bitti < len(binaari_teksti):
        if binaari_teksti[bitti] == '0':
            apumuuttuja += '0'
            vali += '0'
            if len(vali) == (8 + nollia_lopussa):
                pakattu_binaari = binaari_teksti[bitti+1:]
                break
            bitti += 1
        else:
            merkki = chr(int(binaari_teksti[bitti+1:bitti+9],2))
            sanakirja[merkki] = apumuuttuja
            apumuuttuja = apumuuttuja[:-1] + '1'
            vali = ''
            bitti += 9
    
    # Dekoodaus
    apumuuttuja = ''
    dekoodattu_teksti = ''
    for bitti in pakattu_binaari:
        apumuuttuja += bitti
        if apumuuttuja in list(sanakirja.values()):
            dekoodattu_teksti += list(sanakirja.keys())[list(sanakirja.values()).index(apumuuttuja)]
            apumuuttuja = ''

    dekoodattu_tiedosto = tiedosto_nimi + '.decoded'
    with open(dekoodattu_tiedosto, 'w') as tiedosto:
        tiedosto.write(dekoodattu_teksti)


if __name__ == "__main__":
    pakattava_tiedosto = os.path.join(
        os.path.dirname(__file__), "tests", "simple_test.txt"
    )
    purettava_tiedosto = os.path.join(
        os.path.dirname(__file__), "tests", "simple_test.txt.huff"
    )
    if len(sys.argv) > 1:
        pakattava_tiedosto = os.path.join(os.getcwd(), sys.argv[1])

    # pakkaa(pakattava_tiedosto)
    pura(purettava_tiedosto)
