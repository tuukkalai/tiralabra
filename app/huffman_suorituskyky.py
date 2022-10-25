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
    testitiedostojen_kansio = os.path.join(os.getcwd(), "data")

    testattavat_tiedostot = [".txt", ".c", ".lsp"]
    testitiedostot = [
        os.path.join(hakemisto, tiedosto)
        for hakemisto, hakemisto_nimi, tiedosto_nimi in os.walk(testitiedostojen_kansio)
        for tiedosto in tiedosto_nimi
        if os.path.splitext(tiedosto)[1] in testattavat_tiedostot
    ]

    print()
    print("Tekstitiedostojen pakkaaminen Huffman-algoritmia käyttäen")
    print()
    print(f"{'Tiedosto':<40}{'Koko alkuperäisestä':<25}{'Aikaa käytetty':<20}")
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
            f"{os.path.basename(pakattu_tiedosto):<40}{tiedostokoko_alkuperaisesta:<25}{aika:<20}"
        )
    print()
    print("---")
    print()
    print("Tekstitiedostojen purkaminen Huffman-algoritmia käyttäen")

    testattavat_tiedostot = [".huff"]
    testitiedostot = [
        os.path.join(hakemisto, tiedosto)
        for hakemisto, hakemisto_nimi, tiedosto_nimi in os.walk(testitiedostojen_kansio)
        for tiedosto in tiedosto_nimi
        if os.path.splitext(tiedosto)[1] in testattavat_tiedostot
    ]

    print()
    print(f"{'Tiedosto':<40}{'Aikaa käytetty':<20}")
    for tiedosto in testitiedostot:
        aloitusaika = time.perf_counter()
        purettu_tiedosto = aja_purku_mittaus(tiedosto)
        lopetusaika = time.perf_counter()
        aika = format((lopetusaika - aloitusaika) * 1000, ".2f") + " ms"
        print(f"{os.path.basename(purettu_tiedosto):<40}{aika:<20}")
    print()


if __name__ == "__main__":
    paaohjelma()
