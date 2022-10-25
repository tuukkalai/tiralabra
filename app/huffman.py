import sys
from tiedosto_palvelu import TiedostoPalvelu


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


def yhdista_teksti_ja_sanakirja(teksti: str, sanakirja: dict) -> None:
    """Yhdistetään muodostettu sanakirja, pakattava teksti, sekä tarvittavat otsaketiedot.

    Yhdistetty tiedosto koostuu seuraavista osista. Osien koot alla, jos koko on rajattu.

    ┌────────────┬───────────────┬───────────┬────────────────────┬───────────────┐
    │ Sanakirjan │ Ylimääräisten │ Sanakirja │ Pakattu teksti     │ Ylimääräiset  │
    │ pituus     │ bittien määrä │           │                    │ bitit         │
    └────────────┴───────────────┴───────────┴────────────────────┴───────────────┘
    └─16 bittiä──┴───3 bittiä────┴───────────┴────────────────────┴──0-7 bittiä───┘

    Args:
        teksti (str): Pakattava teksti, syöte.
        sanakirja (dict): Muodostettu sanakirja, jonka avulla syöte muutetaan pakatuksi tekstiksi.
    """

    global koodattava_teksti

    pakattu_teksti = ""
    for c in teksti:
        pakattu_teksti += sanakirja[c]

    ylimaaraiset_bitit = (3 + len(koodattava_teksti) + len(pakattu_teksti)) % 8

    # print('yhdistä, sanakirjan_pituus', format(len(koodattava_teksti), "016b"))
    # print('yhdistä, ylimääräisiä bittejä', format(ylimaaraiset_bitit, "03b"))

    koodattava_teksti = (
        format(len(koodattava_teksti), "016b")
        + format(ylimaaraiset_bitit, "03b")
        + koodattava_teksti
        + pakattu_teksti
        + "0" * ylimaaraiset_bitit
    )

    # print('pakattu_teksti', pakattu_teksti[:64])
    # print("len(koodattava_teksti)", len(koodattava_teksti))


def pakkaa(tiedosto_nimi: str) -> str:
    """Pää pakkausohjelma. Lukee annetun tiedoston, laskee käytettyjen merkkien määrät, muodostaa huffman_puun avulla merkkien ja binäärikoodien sanakirjan. Tulostaa ja palauttaa sanakirjan.

    Args:
        tiedosto_nimi (str): Käsiteltävän tiedoston nimi.

    Returns:
        str: Palauttaa pakatun tiedoston nimen.
    """
    global koodattava_teksti

    tiedosto = TiedostoPalvelu(tiedosto_nimi)
    tiedosto_sisalto = tiedosto.lue_tiedosto()

    merkit = esiintyvyys_laskin(tiedosto_sisalto)
    solmut = merkit
    bitti_koodi_sanakirja = huffman_puu(solmut)
    # print('sanakirja', bitti_koodi_sanakirja)

    yhdista_teksti_ja_sanakirja(tiedosto_sisalto, bitti_koodi_sanakirja)

    numero_lista = []
    for b in range(0, len(koodattava_teksti), 8):
        numero_lista.append(int(koodattava_teksti[b : b + 8], 2))

    tiedosto = tiedosto.kirjoita_tiedosto(numero_lista, "w+b", "huffman")

    koodattava_teksti = ""

    return str(tiedosto)


def pura(tiedosto_nimi: str) -> str:
    """Pakatun tiedoston purku.
    Tiedoston sisältö luetaan muuttujaan tiedosto_sisalto, josta siitä käsitellään binäärimuotoinen esitys.
    Binäärimuotoisen tekstin kaksi ensimmäistä tavua (16 bittiä) kertoo kuinka pitkä sanakirja on.
    Seuraavat 3 bittiä kertovat loppuun lisättyjen bittien määrän.
    Sanakirja muodostetaan binääridatasta Postorder Traversal algoritmilla. Tuloksena dict tyyppinen sanakirja.
    Sanakirjan ja binäärimuotoisen pakatun tekstin avulla saadaan palautettua pakattu tiedosto.
    Purettu tiedosto tallennetaan TiedostoPalvelun avulla.

    Args:
        tiedosto_nimi (str): Purettava tiedosto

    Returns:
        str: Palauttaa puretun tiedoston nimen
    """

    tiedosto = TiedostoPalvelu(tiedosto_nimi)
    tiedosto_sisalto = tiedosto.lue_tiedosto()
    # print(tiedosto_sisalto[:20])

    # Binäärimuotoinen esitys
    binaari_teksti = ""
    for tavu in tiedosto_sisalto:
        binaari_teksti += format(tavu, "08b")

    # print("pura, binaari_teksti", binaari_teksti[:40])

    # Poistetaan tiedot sanakirjan pituudesta ja loppuun lisätyistä ylimääräisistä biteistä
    sanakirjan_pituus = int(binaari_teksti[:16], 2)
    binaari_teksti = binaari_teksti[16:]

    ylimaaraiset_bitit = int(binaari_teksti[:3], 2)
    binaari_teksti = binaari_teksti[3:]

    # print("sanakirjan_pituus", sanakirjan_pituus)
    # print("ylimaaraiset_bitit", ylimaaraiset_bitit)

    sanakirja = {}
    apumuuttuja = ""
    bitti = 0

    # Muodostetaan Postorder traversal -algoritmilla binääridatasta sanakirja
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

    # print('sisalto', binaari_teksti[sanakirjan_pituus:700])
    # print(sanakirja)

    # Dekoodataan sanakirjan avulla pakattu teksti
    apumuuttuja = ""
    dekoodattu_teksti = ""
    for bitti in binaari_teksti[sanakirjan_pituus:-ylimaaraiset_bitit]:
        apumuuttuja += bitti
        if apumuuttuja in list(sanakirja.values()):
            dekoodattu_teksti += list(sanakirja.keys())[
                list(sanakirja.values()).index(apumuuttuja)
            ]
            apumuuttuja = ""

    # print('purettu teksti kirjoitettavaksi', dekoodattu_teksti[:64])

    tiedosto = tiedosto.kirjoita_tiedosto(dekoodattu_teksti, "w", "huffman")
    return str(tiedosto)


def kayttoohje():
    return f"\n\
    Tekstitiedoston pakkaaminen ja purkaminen Huffman-algoritmilla\n\
    \n\
    ┌──────────────────────────────────────────────────────────┐\n\
    │  Käyttö:                                                 │\n\
    │    poetry run python app/huffman.py [vipu] [tiedosto]    │\n\
    └──────────────────────────────────────────────────────────┘\n\
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

    vipu = sys.argv[1]

    if vipu == "-c":
        pakattu_tiedosto = pakkaa(sys.argv[2])
        print("Pakattu tiedosto:", pakattu_tiedosto)

    if vipu == "-d":
        purettu_tiedosto = pura(sys.argv[2])
        print("Purettu tiedosto:", purettu_tiedosto)

    if vipu == "-h":
        kayttoohje()


if __name__ == "__main__":
    paaohjelma()
