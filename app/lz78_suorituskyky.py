import os
import time
import lz78


def aja_pakkaus_mittaus(tiedosto_sijainti: str) -> str:
    pakattu = lz78.pakkaa(tiedosto_sijainti)
    return pakattu


def aja_purku_mittaus(tiedosto_sijainti: str) -> str:
    purettu = lz78.pura(tiedosto_sijainti)
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

    # testitiedostot = [
    #     "/home/tuukkala/Documents/koulu/Tietorakenteet_ja_algoritmit_labra_TKT20010/tiralabra/data/sia_cheap_thrills.txt",
    #     "/home/tuukkala/Documents/koulu/Tietorakenteet_ja_algoritmit_labra_TKT20010/tiralabra/data/jfk_virkaanastujaispuhe.txt",
    #     "/home/tuukkala/Documents/koulu/Tietorakenteet_ja_algoritmit_labra_TKT20010/tiralabra/data/simple_test.txt",
    #     "/home/tuukkala/Documents/koulu/Tietorakenteet_ja_algoritmit_labra_TKT20010/tiralabra/data/canterbury_corpus/fields.c",
    #     "/home/tuukkala/Documents/koulu/Tietorakenteet_ja_algoritmit_labra_TKT20010/tiralabra/data/canterbury_corpus/grammar.lsp",
    # ]

    print()
    print("Tekstitiedostojen pakkaaminen LZ78-algoritmia käyttäen")
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
    print("Tekstitiedostojen purkaminen LZ78-algoritmia käyttäen")

    testattavat_tiedostot = [".lz"]
    testitiedostot = [
        os.path.join(hakemisto, tiedosto)
        for hakemisto, hakemisto_nimi, tiedosto_nimi in os.walk(testitiedostojen_kansio)
        for tiedosto in tiedosto_nimi
        if os.path.splitext(tiedosto)[1] in testattavat_tiedostot
    ]
    # testitiedostot = ['/home/tuukkala/Documents/koulu/Tietorakenteet_ja_algoritmit_labra_TKT20010/tiralabra/data/jfk_virkaanastujaispuhe.txt.lz']

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
