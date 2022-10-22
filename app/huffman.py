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


def yhdista_teksti_ja_sanakirja(teksti: str, sanakirja: dict) -> None:
    """Lisätään globaalin muuttujan (koodattava_teksti) alkuun info (3-bit) kuinka monta nollaa poistetaan sanakirjan lopusta. Sanakirja (Huffman puu) osuuden loppuun lisätään nollia niin, että tulee 8-bittiä nollia -> sanakirja loppuu ja pakattu teksti alkaa.
    otsake = 3-bittiä,
    sanakirja = tarvittava määrä tavuja, lopussa otsakkeen merkitsemä määrä nollia
    erottaja = tavullinen nollia
    pakattu_teksti = sanakirjan avulla koottu pakattava teksti
    """
    global koodattava_teksti

    pakattu_teksti = ""
    for c in teksti:
        pakattu_teksti += sanakirja[c]

    koodattava_teksti = (
        format(len(koodattava_teksti), "016b") + koodattava_teksti + pakattu_teksti
    )


def pakkaa(tiedosto_nimi: str) -> str:
    """Pää pakkausohjelma. Lukee annetun tiedoston, laskee käytettyjen merkkien määrät, muodostaa huffman_puun avulla merkkien ja binäärikoodien sanakirjan. Tulostaa ja palauttaa sanakirjan.

    Args:
        tiedosto_nimi (str): Käsiteltävän tiedoston nimi.

    Returns:
        str: Palauttaa pakatun tiedoston nimen
    """

    teksti = lue_tiedosto(tiedosto_nimi)
    merkit = esiintyvyys_laskin(teksti)
    solmut = merkit
    bitti_koodi_sanakirja = huffman_puu(solmut)

    yhdista_teksti_ja_sanakirja(teksti, bitti_koodi_sanakirja)

    numero_lista = []
    for b in range(0, len(koodattava_teksti), 8):
        numero_lista.append(int(koodattava_teksti[b : b + 8], 2))

    pakattu_tiedosto = tiedosto_nimi + ".huff"
    with open(pakattu_tiedosto, "wb") as tiedosto:
        tiedosto.write(bytearray(numero_lista))

    return pakattu_tiedosto


def pura(tiedosto_nimi: str) -> str:
    """Pakatun tiedoston purku.
    Tiedoston sisältö luetaan muuttujaan teksti, josta siitä käsitellään binäärimuotoinen esitys.
    Binäärimuotoisen tekstin kaksi ensimmäistä tavua (16 bittiä) kertoo kuinka pitkä sanakirja on.
    Sanakirja käydään läpi postorder traversal algoritmilla, jolla saadaan palautettua dict tyyppinen sanakirja.
    Sanakirjan ja lopun binäärimuotoisen "tekstin" avulla saadaan palautettua pakattu tiedosto.

    Args:
        tiedosto_nimi (str): Purettava tiedosto

    Returns:
        str: Palauttaa puretun tiedoston nimen
    """

    # Tiedoston lukeminen
    with open(tiedosto_nimi, "rb") as tiedosto:
        teksti = tiedosto.read()

    # Binäärimuotoinen esitys
    binaari_teksti = ""
    for tavu in teksti:
        binaari_teksti += format(tavu, "08b")

    sanakirjan_pituus = int(binaari_teksti[:16], 2)
    binaari_teksti = binaari_teksti[16:]

    sanakirja = {}
    apumuuttuja = ""
    bitti = 0

    # Postorder traversal
    while bitti < sanakirjan_pituus:
        if binaari_teksti[bitti] == "0":
            apumuuttuja += "0"
            bitti += 1
        else:
            merkki = chr(int(binaari_teksti[bitti + 1 : bitti + 9], 2))
            sanakirja[merkki] = apumuuttuja
            while len(apumuuttuja) > 0 and apumuuttuja[-1] == "1":
                apumuuttuja = apumuuttuja[:-1]
            apumuuttuja = apumuuttuja[:-1] + "1"
            bitti += 9

    # Dekoodaus
    apumuuttuja = ""
    dekoodattu_teksti = ""
    for bitti in binaari_teksti[sanakirjan_pituus:]:
        apumuuttuja += bitti
        if apumuuttuja in list(sanakirja.values()):
            dekoodattu_teksti += list(sanakirja.keys())[
                list(sanakirja.values()).index(apumuuttuja)
            ]
            apumuuttuja = ""

    dekoodattu_tiedosto = tiedosto_nimi + ".purettu"
    with open(dekoodattu_tiedosto, "w") as tiedosto:
        tiedosto.write(dekoodattu_teksti)

    return dekoodattu_tiedosto


def kayttoohje():
    return f"\n\
    Tekstitiedoston pakkaaminen ja purkaminen Huffman-algoritmilla\n\
    \n\
    ┌──────────────────────────────────────────────────────────┐\n\
    │  Käyttö:                                                 │\n\
    │    poetry run invoke huffmanpakkaa [tiedosto]            │\n\
    │    poetry run invoke huffmanpura [tiedosto]              │\n\
    └──────────────────────────────────────────────────────────┘\n\
    \n\
    Sovelluksen voi käynnistää myös ilman poetryn komentoja:\n\
      python3 app/huffman.py [vipu] [tiedosto]\n\
    \n\
    Vivut:\n\
      -c{' ' * 10}pakkaa annettu tiedosto\n\
      -d{' ' * 10}pura annettu tiedosto\n\
      -h{' ' * 10}näytä ohje\n\
    "

def paaohjelma():
    if len(sys.argv) < 3:
        print(kayttoohje())
        return

    tiedosto = os.path.join(os.getcwd(), sys.argv[2])

    if not os.path.isfile(tiedosto) and not os.path.isfile(sys.argv[2]):
        print(f"Tiedostoa {sys.argv[2]} ei löydy.")
        return

    vipu = sys.argv[1]

    if vipu == "-c":
        pakattu = pakkaa(tiedosto)
        print(f"Pakattu tiedosto tallennettu {pakattu}")

    if vipu == "-d":
        purettu = pura(tiedosto)
        print(f"Purettu tiedosto tallennettu {purettu}")

    if vipu == "-h":
        print(kayttoohje())


if __name__ == "__main__":
    paaohjelma()
