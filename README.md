# Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (periodi I), Laboratoriotyöskentely

![CI Status](https://github.com/tuukkalai/tiralabra/workflows/CI/badge.svg)
[![codecov](https://img.shields.io/codecov/c/gh/tuukkalai/tiralabra)](https://codecov.io/gh/tuukkalai/tiralabra)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Dokumentaatio

### Viikkoraportit

- [Viikko 1](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko1.md)
- [Viikko 2](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko2.md)
- [Viikko 3](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko3.md)
- [Viikko 4](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko4.md)
- [Viikko 5](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko5.md)
- [Viikko 6](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko6.md)

### Muut

- [Määrittelydokumentti](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/testausdokumentti.md)

## Projektin riippuvuudet

Sovelluksen käyttämät tiedostot sijaitsevat hakemistossa `app`.

Riippuvuuksien hallinnan tueksi projektiin on tuotu **Poetry**. Jos Poetry ei ole asennettuna koneellesi, aloita seuraamalla [Ohjelmistotekniikka-kurssin ohjeita aiheesta](https://ohjelmistotekniikka-hy.github.io/python/viikko2#poetry-ja-riippuvuuksien-hallinta).

Kun Poetry on asennettu, asenna riippuvuudet komennolla

```sh
poetry install
```

## Projektin suorittaminen

Pakkaa tiedosto Huffman-algoritmilla

```sh
poetry run invoke huffmanpakkaa --tiedosto=[tiedosto]
# tai
poetry run python app/huffman.py -c [tiedosto]
```

Pura tiedosto Huffman-algoritmilla

```sh
poetry run invoke huffmanpura --tiedosto=[tiedosto]
# tai
poetry run python app/huffman.py -d [tiedosto]
```

Pakkaa tiedosto LZ78-algoritmilla

```sh
poetry run invoke lzpakkaa --tiedosto=[tiedosto]
# tai
poetry run python app/lz78.py -c [tiedosto]
```

Pura tiedosto LZ78-algoritmilla

```sh
poetry run invoke lzpura --tiedosto=[tiedosto]
# tai
poetry run python app/lz78.py -d [tiedosto]
```

## Muita hyödyllisiä komentoja

### Testit saa suoritettua komennolla

```sh
poetry run invoke test
```

### Suorituskykytestit

Suorituskyvyn testaamista varten on hakemistoon `data` lisätty muutamia testitiedostoja, joita voidaan pakata ja purkaa seuraavalla komennolla

```sh
poetry run invoke suorituskyky
```

### Luo testikattavuuden raportti

```sh
poetry run invoke coverage-report
```

### Luo selaimella luettava testikattavuuden raportti

```sh
poetry run invoke coverage-html
```

### Aja koodin tyylin muotoilun työkalu ([Black](https://black.readthedocs.io/en/stable/index.html))

```sh
poetry run invoke format
```
### Poista pakatut ja puretut tiedostot data-hakemistosta

```sh
poetry run invoke siivoa
```
