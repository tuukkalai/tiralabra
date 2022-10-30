# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

Yksikkötestauksen kattavuusprosentti on nähtävillä projektin [README:ssä GitHubissa](https://github,com/tuukkalai/tiralabra), sekä [Codecov:ssa](https://app.codecov.io/gh/tuukkalai/tiralabra).

## Mitä on testattu, miten tämä tehtiin?

Testauksessa on keskitytty vain ohjelman keskeisiin osiin, eli `app`-kansion tiedostoihin (pl. app/tests). Testaus on toteutettu [pytest](https://pypi.org/project/pytest/)-kirjaston avulla.

## Minkälaisilla syötteillä testaus tehtiin

Testausta tehtiin ASCII-merkistöä käyttävillä tekstitiedostoilla. Testattavat tiedostot sisältävät eri asteisesti toisteisuutta, sekä sisältävät eri tyyppistä tekstiä, luonnollista kieltä (englantia) sekä koodia (c, html, lisp).

## Miten testit voidaan toistaa

Testit voidaan toistaa komennolla

```sh
poetry run invoke test
```

Suorituskykytestejä voidaan ajaa komennolla

```sh
python app/huffman_suorituskyky.py && python app/lz78_suorituskyky.py
# tai hieman hitaampi tapa
poetry run invoke suorituskyky
```

## Ohjelman toiminnan empiirisen testauksen tulosten esittäminen

[Tiedostosta `vertailu`](vertailu.csv) löytyy taulukoituna algoritmien suorituskykyvertailu. Molemmat algoritmit onnistuvat pakkaamaan suurehkon tiedoston 50-60 % alkuperäisestä koosta. Vaihtelu algoritmien ja tiedostojen välillä selittyy pakattavan tiedoston sisällöllä.

Ajallisesti Huffman-algoritmi pakkaa tiedostot nopeammin ja LZ78-algoritmi purkaa tiedostot nopeammin. Ero ei ole kuitenkaan suuri, ja tässäkin ilmenee vaihtelua joka riippuu pakattavan ja purettavan tiedoston sisällöstä.

Suorituskykytestausta suoritettaessa kannattaa huomioida, että poetryn kanssa ajettuna testit kestävät kauemmin.
