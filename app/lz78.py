import sys
from tiedosto_palvelu import TiedostoPalvelu


def pakkaa(teksti: str) -> bytearray:
    """pakkaa() lukee annetun merkkijonon ja palauttaa LZ78-algoritmilla koodatun merkkijonon.

    Args:
        teksti (str): Syöte, annettu merkkijono

    Returns:
        bytearray: Bittilista
    """
    sanakirja = {}
    apumuuttuja = ""
    enkoodattavat_sijainnit = []
    seuraavat_merkit = []
    i = 0
    sijainti = 1
    while i < len(teksti):
        apumuuttuja += teksti[i]
        if apumuuttuja not in sanakirja or (i+1) == len(teksti):
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

    return bytearray(sijainti_merkki_lista)


def pura(pakattu_teksti: bytearray) -> str:
    sijainnit = []
    seuraavat_merkit = []
    sanakirja = []
    for i in range(len(pakattu_teksti)):
        if i % 2 == 0:
            sijainnit.append(pakattu_teksti[i])
            if pakattu_teksti[i] == 0:
                sanakirja.append(chr(pakattu_teksti[i+1]))
            else:
                sanakirja.append(str(sanakirja[pakattu_teksti[i]-1]) + chr(pakattu_teksti[i+1]))
        else:
            seuraavat_merkit.append(chr(pakattu_teksti[i]))
    
    return "".join(sanakirja)


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

    tiedosto = TiedostoPalvelu(sys.argv[2])

    vipu = sys.argv[1]

    if vipu == "-c":
        binaari = pakkaa(tiedosto.lue_tiedosto())
        pakattu_tiedosto = TiedostoPalvelu(str(tiedosto))
        pakattu_tiedosto.kirjoita_tiedosto(binaari, 'w+b')

    if vipu == "-d":
        purettu = pura(tiedosto.lue_tiedosto())
        purettu_tiedosto = TiedostoPalvelu(str(tiedosto))
        purettu_tiedosto.kirjoita_tiedosto(purettu, 'w')

    if vipu == "-h":
        kayttoohje()


if __name__ == "__main__":
    paaohjelma()
