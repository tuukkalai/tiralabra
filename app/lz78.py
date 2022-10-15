import os
import sys
from tiedosto_palvelu import TiedostoPalvelu


def pakkaa(teksti: str) -> str:
    sanakirja = {}
    apumuuttuja = ""
    enkoodattavat_sijainnit = []
    seuraavat_merkit = []
    i = 0
    sijainti = 1
    while i < len(teksti):
        apumuuttuja += teksti[i]
        if apumuuttuja not in sanakirja:
            sanakirja[apumuuttuja] = sijainti
            sijainti += 1
            if len(apumuuttuja) > 1 and apumuuttuja[:-1] in sanakirja:
                enkoodattavat_sijainnit.append(sanakirja[apumuuttuja[:-1]])
            else:
                enkoodattavat_sijainnit.append(0)
            seuraavat_merkit.append(apumuuttuja[-1:])
            apumuuttuja = ""
        i += 1
    pakattu_teksti = ""
    for i in range(len(enkoodattavat_sijainnit)):
        pakattu_teksti += str(enkoodattavat_sijainnit[i]) + seuraavat_merkit[i]
    return pakattu_teksti


def pura(pakattu_teksti: str) -> str:
    sijainnit = []
    seuraavat_merkit = []
    for i in range(len(pakattu_teksti)):
        try:
            osoitin = int(pakattu_teksti[i])
        except ValueError:
            seuraavat_merkit.append(pakattu_teksti[i])
        else:
            print("osoitin on ", osoitin, " ja tyyppiä ", type(osoitin))
            sijainnit.append(osoitin)
    print("sijainnit", sijainnit)
    print("merkit", seuraavat_merkit)


def kayttoohje():
    print()
    print("Tekstitiedoston pakkaaminen ja purkaminen LZ78-algoritmilla")
    print()
    print("┌──────────────────────────────────────────────────────────┐")
    print("│  Käyttö:                                                 │")
    print("│    poetry run invoke lzpakkaa [tiedosto]                 │")
    print("│    poetry run invoke lzpura [tiedosto]                   │")
    print("└──────────────────────────────────────────────────────────┘")
    print()
    print("Sovelluksen voi käynnistää myös ilman poetryn komentoja:")
    print("  python3 app/lz78.py [vipu] [tiedosto]")
    print()
    print("Vivut:")
    print("  -c", " " * 10, "pakkaa annettu tiedosto")
    print("  -d", " " * 10, "pura annettu tiedosto")
    print("  -h", " " * 10, "näytä ohje")
    print()


def paaohjelma():
    if len(sys.argv) < 3:
        kayttoohje()
        return

    tiedosto = TiedostoPalvelu(sys.argv[2])

    vipu = sys.argv[1]

    if vipu == "-c":
        pakattu = pakkaa(tiedosto.lue_tiedosto())
        print(f"Pakattu tiedosto tallennettu {pakattu}")

    if vipu == "-d":
        purettu = pura(tiedosto)
        print(f"Purettu tiedosto tallennettu {purettu}")

    if vipu == "-h":
        kayttoohje()


if __name__ == "__main__":
    paaohjelma()
