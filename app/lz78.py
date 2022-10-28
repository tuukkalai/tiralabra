import sys
from tiedosto_palvelu import TiedostoPalvelu


def pakkaa(tiedosto_nimi: str) -> str:
    """Metodi pakkaa lukee annetun tiedoston sisällön ja palauttaa LZ78-algoritmilla pakatun tiedoston sijainnin.

    Pakkausalgoritmi muodostaa ketjun sijainteja ja seuraavia merkkejä seuraavalla formaatilla:

        ┌────────────────┬────────────────┬─────────────┐
    ... │ Sijainti (MSB) │ Sijainti (LSB) │ Merkki      │ ...
        └────────────────┴────────────────┴─────────────┘
        └────8 bittiä────┴────8 bittiä────┴──8 bittiä───┘

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
        sijainti_merkki_lista.append(
            int(format(enkoodattavat_sijainnit[i], "016b")[:8], 2)
        )
        sijainti_merkki_lista.append(
            int(format(enkoodattavat_sijainnit[i], "016b")[8:], 2)
        )
        sijainti_merkki_lista.append(ord(seuraavat_merkit[i]))
        # print(sijainti_merkki_lista[-3:])

    tiedosto.kirjoita_tiedosto(sijainti_merkki_lista, "w+b", "lz")
    return str(tiedosto)


def pura(tiedosto_nimi: str) -> str:
    tiedosto = TiedostoPalvelu(tiedosto_nimi)
    tiedosto_sisalto = tiedosto.lue_tiedosto()

    sijainnit = []
    seuraavat_merkit = []
    sanakirja = []
    for i in range(len(tiedosto_sisalto)):
        if i % 3 == 0:
            sijainti = int(
                format(tiedosto_sisalto[i], "08b")
                + format(tiedosto_sisalto[i + 1], "08b"),
                2,
            )
            sijainnit.append(sijainti)
            if sijainti == 0:
                sanakirja.append(chr(tiedosto_sisalto[i + 2]))
            else:
                sanakirja.append(
                    str(sanakirja[sijainti - 1]) + chr(tiedosto_sisalto[i + 2])
                )
        elif i % 3 == 2:
            seuraavat_merkit.append(chr(tiedosto_sisalto[i]))


    tiedosto.kirjoita_tiedosto("".join(sanakirja))
    return str(tiedosto)


def kayttoohje():
    return f"\n\
    Tekstitiedoston pakkaaminen ja purkaminen LZ78-algoritmilla\n\
    \n\
    ┌──────────────────────────────────────────────────────────┐\n\
    │  Käyttö:                                                 │\n\
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
