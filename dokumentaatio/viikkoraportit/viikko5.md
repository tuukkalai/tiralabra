# Viikkoraportti - viikko 5

> Mitä olen tehnyt tällä viikolla?

Viikon aikana sain luotua toimivan Huffman puun esitysmuodon pakatun tiedoston alkuun tai loppuun. Pakattavien merkkien bittimäärän vaihtelun vuoksi tiedoston loppuun saattaa ilmestyä ylimääräisiä merkkejä pakkaamisen ja purkamisen jälkeen.

Lempel-Ziv 78 algoritmin toimintamalli on selkeä, enää puuttuu itse toteutus.

> Miten ohjelma on edistynyt?

Ohjelmaan on saatu Huffman puun lisääminen binääritiedostoon. Pakatun tiedoston purkaminen toimii myös, kuitenkin joitain virheitä on edelleen havaittavissa, muun muassa tiedoston loppuun saattaa muodostua ylimääräisiä 0-bittejä, jotka sanakirjasta riippuen saatetaan tulkita pakatuiksi merkeiksi. Tähän auttanee pakaamattoman tiedoston pituudesta kertova tavu tiedoston headeriin.

> Mitä opin tällä viikolla / tänään?

Muutamia hyviä oivalluksia tuli havaittua kun luki vertaisarvioitavan projektin koodia ja projektin rakennetta. Vaikka oman sovellukseni ydinfunktio saattaa olla puoli askelta edellä vertaisarvioitavaa työtä, on kaikki muu projektin ympärillä paljon jäljessä. Projektin jatkokehitys hidastuu varmasti, ellen käytä enemmän aikaa projektin strukturointiin ja testien tekemiseen.

> Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

Ei selkeitä vaikeuksia/ongelmia.

> Mitä teen seuraavaksi?

Seuraavaksi viikoksi tavoitteena LZ78 algoritmin edistämistä ja paranneltu projektin struktuuri. Sekä testikattavuuden nostaminen paremmalle tasolle.

## Tuntikirjanpito

|PVM|Mitä tein?|Aikaa käytetty (h)|
|:--|:--|:--|
|4.10.|Huffman-puun kirjoittaminen tiedostoon.|6|
|5.10.|Huffman-puun lukeminen tiedoston alusta ja pakatun tiedoston purkaminen Huffman-puun avulla|6|
|8.10.|LZ78-algoritmin työstön aloittaminen ([app/lz78.py](https://github.com/tuukkalai/tiralabra/blob/main/app/lz78.py)), viikkoraportin kirjoittaminen|3|
|||yht. 15|
