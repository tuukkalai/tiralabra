import os
import time
import huffman


def aja_pakkaus_mittaus(tiedosto_sijainti: str) -> str:
    pakattu = huffman.pakkaa(tiedosto_sijainti)
    return pakattu


def aja_purku_mittaus(tiedosto_sijainti: str) -> tuple:
    purettu = huffman.pura(tiedosto_sijainti)
    return purettu


def paaohjelma():
    testattava_joukko = "canterbury_corpus"
    testattavat_tiedostot = [".txt"]

    testitiedostojen_kansio = os.path.join(os.getcwd(), "data", testattava_joukko)

    testitiedostot = [
        os.path.join(testitiedostojen_kansio, tiedosto)
        for tiedosto in os.listdir(testitiedostojen_kansio)
        if os.path.splitext(tiedosto)[1] in testattavat_tiedostot
    ]

    print("Tekstitiedostojen pakkaaminen Huffman-algoritmiä käyttäen")
    print()
    print(f"{'Tiedosto':<30}{'Koko alkuperäisestä':<20}{'Aikaa käytetty':<20}")
    for tiedosto in testitiedostot:
        aloitusaika = time.perf_counter()
        pakattu_tiedosto = aja_pakkaus_mittaus(tiedosto)
        lopetusaika = time.perf_counter()
        tiedostokoko_alkuperaisesta = (
            format(
                (os.path.getsize(pakattu_tiedosto) / os.path.getsize(tiedosto)) * 100,
                ".2f",
            )
            + " %"
        )
        aika = format((lopetusaika - aloitusaika) * 1000, ".2f") + " ms"
        print(
            f"{os.path.basename(pakattu_tiedosto):<30}{tiedostokoko_alkuperaisesta:<20}{aika:<20}"
        )
    print()
    print("---")
    print()
    print("Tekstitiedostojen purkaminen Huffman-algoritmiä käyttäen")

    testattavat_tiedostot = [".huff"]
    testitiedostot = [
        os.path.join(testitiedostojen_kansio, tiedosto)
        for tiedosto in os.listdir(testitiedostojen_kansio)
        if os.path.splitext(tiedosto)[1] in testattavat_tiedostot
    ]

    print()
    print(f"{'Tiedosto':<30}{'Aikaa käytetty':<20}")
    for tiedosto in testitiedostot:
        aloitusaika = time.perf_counter()
        purettu_tiedosto = aja_purku_mittaus(tiedosto)
        lopetusaika = time.perf_counter()
        aika = format((lopetusaika - aloitusaika) * 1000, ".2f") + " ms"
        print(f"{os.path.basename(purettu_tiedosto):<30}{aika:<20}")


if __name__ == "__main__":
    paaohjelma()
