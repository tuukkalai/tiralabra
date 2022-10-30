import sys
from tiedosto_palvelu import TiedostoPalvelu


def pakkaa(tiedosto_nimi: str) -> str:
    """Metodi pakkaa lukee annetun tiedoston sisällön ja palauttaa LZ78-algoritmilla pakatun tiedoston sijainnin.

    Pakkausalgoritmi muodostaa ketjun sijainteja ja seuraavia merkkejä seuraavalla formaatilla:

        ┌───────────────────────────────┬─────────────┐
    ... │ Sijainti (Pienin mahdollinen  │ Merkki      │ ...
        │   bittimäärä)                 │             │
        └───────────────────────────────┴─────────────┘
        └────1-k bittiä─────────────────┴──8 bittiä───┘

    Merkitään sijainti mahdollisimman vähällä määrällä bittejä
        -> alla olevan esimerkin viimeinen rivi

    Esimerkkisyöte:
    A|B|C|AB|CA|BC|ABC|CC|BA|ABCA|BB|ABCAB|A

    1    10    11    100    101   110   111    1000    1001    1010    1011    1100
    <0,A><0,B>|<00,C><01,B>|<11,A><10,C><100,C><011,C>|<0010,A><0111,A><0010,B><1001,B> <0000,A>
    0,1       |00,01,10,11 |000,001,...,111           |0000,0001,...,1111

    Args:
        teksti (str): Pakattavan tiedoston nimi.

    Returns:
        str: Pakatun tiedoston nimi.
    """
    tiedosto = TiedostoPalvelu(tiedosto_nimi)
    tiedosto_sisalto = tiedosto.lue_tiedosto()

    sanakirja = {}
    apumuuttuja = ""
    enkoodattavat_sijainnit = []
    seuraavat_merkit = []
    i = 0
    sijainti = 1

    # Pakattavan tiedosto sisältö käydään läpi merkki merkiltä, ja lisätään sanakirjaan aiemmin tuntemattomat merkkijonot
    while i < len(tiedosto_sisalto):
        apumuuttuja += tiedosto_sisalto[i]
        if apumuuttuja not in sanakirja or (i + 1) == len(tiedosto_sisalto):
            sanakirja[apumuuttuja] = sijainti
            sijainti += 1
            if len(apumuuttuja) > 1 and apumuuttuja[:-1] in sanakirja:
                enkoodattavat_sijainnit.append(sanakirja[apumuuttuja[:-1]])
            else:
                enkoodattavat_sijainnit.append(0)
            seuraavat_merkit.append(apumuuttuja[-1:])
            apumuuttuja = ""
        i += 1

    # Yhdistetään lista sijainteja ja merkkejä
    sijainti_merkki_lista = []
    for i in range(len(enkoodattavat_sijainnit)):
        pituus = "0" + str(len(format(i, "b"))) + "b"
        sijainti_merkki_lista.append(format(enkoodattavat_sijainnit[i], pituus))
        sijainti_merkki_lista.append(format(ord(seuraavat_merkit[i]), "08b"))

    yhdistetty_binaari = "".join(sijainti_merkki_lista)
    yhdistetty_binaari += "0" * (len(yhdistetty_binaari) % 8)

    tavutettu = []
    for i in range(0, len(yhdistetty_binaari), 8):
        tavutettu.append(int(yhdistetty_binaari[i : i + 8], 2))

    tiedosto.kirjoita_tiedosto(tavutettu, "w+b", "lz")
    return str(tiedosto)


def pura(tiedosto_nimi: str) -> str:
    tiedosto = TiedostoPalvelu(tiedosto_nimi)
    tiedosto_sisalto = tiedosto.lue_tiedosto()

    sisalto_arr = []
    for i in range(len(tiedosto_sisalto)):
        sisalto_arr.append(format(tiedosto_sisalto[i], "08b"))

    sisalto_bin = "".join(sisalto_arr)

    sijainnit = []
    seuraavat_merkit = []
    sanakirja = []

    i = 0
    j = 0
    while len(sisalto_bin) > 0:
        if i % 2 == 0:
            pituus = len(format(j, "b"))
            sijainti = int(sisalto_bin[:pituus], 2)
            sijainnit.append(sijainti)
            if len(sisalto_bin) < pituus + 8:
                break
            if sijainti == 0:
                kirjain = chr(int(sisalto_bin[pituus : pituus + 8], 2))
                sanakirja.append(kirjain)
            else:
                sanakirja.append(
                    str(sanakirja[sijainti - 1])
                    + chr(int(sisalto_bin[pituus : pituus + 8], 2))
                )
            sisalto_bin = sisalto_bin[pituus:]
            j += 1
        else:
            kirjain = chr(int(sisalto_bin[:8], 2))
            seuraavat_merkit.append(kirjain)
            sisalto_bin = sisalto_bin[8:]
        i += 1

    tiedosto.kirjoita_tiedosto("".join(sanakirja))
    return str(tiedosto)


def kayttoohje():
    return f"\n\
    Tekstitiedoston pakkaaminen ja purkaminen LZ78-algoritmilla\n\
    \n\
    ┌──────────────────────────────────────────────────────────┐\n\
    │  Käyttö:                                                 │\n\
    │    poetry run invoke lzpakkaa --tiedosto=[tiedosto]      │\n\
    │    poetry run invoke lzpura --tiedosto=[tiedosto]        │\n\
    │    poetry run python app/lz78.py [vipu] [tiedosto]       │\n\
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
