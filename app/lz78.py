import sys
from tiedosto_palvelu import TiedostoPalvelu


def pakkaa(tiedosto_nimi: str) -> str:
    """pakkaa() lukee annetun merkkijonon ja palauttaa LZ78-algoritmilla koodatun merkkijonon.

    Args:
        teksti (str): Syöte, annettu merkkijono

    Returns:
        bytearray: Bittilista
    """
    tiedosto = TiedostoPalvelu(tiedosto_nimi)
    tiedosto_sisalto = tiedosto.lue_tiedosto()

    sanakirja = {}
    apumuuttuja = ""
    enkoodattavat_sijainnit = []
    seuraavat_merkit = []
    i = 0
    sijainti = 1
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

    sijainti_merkki_lista = []
    for i in range(len(enkoodattavat_sijainnit)):
        sijainti_merkki_lista.append(enkoodattavat_sijainnit[i])
        sijainti_merkki_lista.append(ord(seuraavat_merkit[i]))

    tiedosto.kirjoita_tiedosto(sijainti_merkki_lista, "w+b")
    return str(tiedosto)


def pura(tiedosto_nimi: str) -> str:
    tiedosto = TiedostoPalvelu(tiedosto_nimi)
    tiedosto_sisalto = tiedosto.lue_tiedosto()

    sijainnit = []
    seuraavat_merkit = []
    sanakirja = []
    for i in range(len(tiedosto_sisalto)):
        if i % 2 == 0:
            sijainnit.append(tiedosto_sisalto[i])
            if tiedosto_sisalto[i] == 0:
                sanakirja.append(chr(tiedosto_sisalto[i + 1]))
            else:
                sanakirja.append(
                    str(sanakirja[tiedosto_sisalto[i] - 1])
                    + chr(tiedosto_sisalto[i + 1])
                )
        else:
            seuraavat_merkit.append(chr(tiedosto_sisalto[i]))

    tiedosto.kirjoita_tiedosto("".join(sanakirja))
    return str(tiedosto)


def kayttoohje():
    return f"\n\
    Tekstitiedoston pakkaaminen ja purkaminen LZ78-algoritmilla\n\
    \n\
    ┌──────────────────────────────────────────────────────────┐\n\
    │  Käyttö:                                                 │\n\
    │    poetry run invoke lzpakkaa [tiedosto]                 │\n\
    │    poetry run invoke lzpura [tiedosto]                   │\n\
    └──────────────────────────────────────────────────────────┘\n\
    \n\
    Sovelluksen voi käynnistää myös ilman poetryn komentoja:\n\
      python3 app/lz78.py [vipu] [tiedosto]\n\
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
