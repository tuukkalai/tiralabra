<<<<<<< HEAD
# Viikkoraportti - viikko 4

> Mitä olen tehnyt tällä viikolla?

Tällä viikolla aika on kulunut edelleen opiskeluun ja selvitystyöhön binääridatan käsittelyyn Pythonilla, sekä LZ78 algoritmin toiminnan opiskeluun.

> Miten ohjelma on edistynyt?

Ohjelmaan on saatu Huffman puun lisääminen binääritiedostoon. Pakatun tiedoston dekoodaus toiminto ei ole vielä valmiina.

> Mitä opin tällä viikolla / tänään?

Puun solmujen välillä kulkeminen preorder traversal, postorder traversal ja inorder traversal algoritmeilla oli melkoisen oppimisen takana.

> Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

Ei selkeitä vaikeuksia. Varmasti jatkossa tulee taas lisää selvitettävää ja kysyttävää.

> Mitä teen seuraavaksi?

Seuraavaksi viikoksi tavoitteena on Huffman-algoritmin dekoodaus funktio, sekä LZ78 algoritmin aloitus.
=======
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
>>>>>>> origin/main

## Tuntikirjanpito

|PVM|Mitä tein?|Aikaa käytetty (h)|
|:--|:--|:--|
<<<<<<< HEAD
|28.9.|Puun solmujen välillä kulkeminen traversal algoritmien avulla.|3|
|30.9.|Huffman-algoritmin työstö ja Huffman-puun lisääminen binääritiedostoon mahdollisesti luettavaan (dekoodattavaan) muotoon|8|
|1.10.|Huffman-algoritmin työstö ja viikkoraportin kirjoittaminen|3|
|||yht. 14|
=======
|4.10.|Huffman-puun kirjoittaminen tiedostoon.|6|
|5.10.|Huffman-puun lukeminen tiedoston alusta ja pakatun tiedoston purkaminen Huffman-puun avulla|6|
|8.10.|LZ78-algoritmin työstön aloittaminen ([branch 'lz'](https://github.com/tuukkalai/tiralabra/blob/lz/app/lz78.py)), viikkoraportin kirjoittaminen|3|
|||yht. 15|
>>>>>>> origin/main
