# Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (periodi I), Laboratoriotyöskentely

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Esitietoja projektista

Sovelluksen käyttämät tiedostot sijaitsevat hakemistossa `app`.

Riippuvuuksien hallinnan tueksi projektiin on tuotu **Poetry**. Jos Poetry ei ole asennettuna koneellesi, aloita seuraamalla [Ohjelmistotekniikka-kurssin ohjeita aiheesta](https://ohjelmistotekniikka-hy.github.io/python/viikko2#poetry-ja-riippuvuuksien-hallinta).

Kun Poetry on asennettu, asenna riippuvuudet komennolla

```sh
poetry install
```

## Projektin suorittaminen

Käynnistä projekti komennolla

```sh
poetry run invoke start
```

## Muita hyödyllisiä komentoja

### Testit saa suoritettua komennolla

```sh
poetry run invoke test
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

## Viikkoraportit

- [Viikko 1](https://github.com/tuukkalai/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko1.md)
