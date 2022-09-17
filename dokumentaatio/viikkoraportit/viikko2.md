# Viikkoraportti - viikko 2

> Mitä olen tehnyt tällä viikolla?

Tällä viikolla olen opiskellut binääridatan käsittelyyn liittyviä tekniikoita Pythonilla. Datan käsittely on haastavaa, mutta vielä haastavampaa tuntuu olevan Huffman puun luoman sanakirjan tallentaminen pakatun tiedoston alkuun.

Binääridatan käsittelyn lisäksi olen edistänyt projektia lisäämällä vaadittuja testejä ja CI-putken. Testejä tulee viilata ja lisätä, mutta en ole tälle suurta painoarvoa antanut, koska projekti saattaa muuttaa muotoaan paljonkin. Tämä rikkoisi testit ja ne tulisi kirjoittaa uudelleen.

> Miten ohjelma on edistynyt?

Ohjelma on jossain määrin edistynyt. Huffman-koodauksesta saa nyt annetulla syötteellä (tiedostolla) muodostettua sanakirjan, jossa jokaiselle merkille on annettu uusi binääriarvo. Tämän sanakirjan avulla annettu syöte tulisi vielä muuttaa binäärimuotoon ja tallentaa Huffman-puun/taulun mukana pakattuun tiedostoon.

> Mitä opin tällä viikolla / tänään?

Viimeisen viikon aikana olen oppinut käsittelemään binääri- ja heksadesimaalidataa Pythonilla, ja sisäistänyt Huffman koodauksen algoritmin.

> Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

Kurssin "Aiheita" sivulla annetuissa vinkeissä Huffman-puu voitaisiin tallentaa [StackOverflow vinkin avulla](https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree), mutta tämä ei tunnu aukeavan.

Miten allaoleva bittisanakirja muuttuu muotoon `001A1C01E01B1D`, ja miten tuosta tiedostoon alkuun lisättävästä muodosta tulisi saada avattua purettu tiedosto?

```txt
A: 00
B: 110
C: 01
D: 111
E: 10
```

[Purdue yliopiston "Advanced C Programming" -kurssin materiaalin](https://engineering.purdue.edu/ece264/17au/hw/HW13?alt=huffman) mukaan **"post-order traversal of the Huffman coding tree"** pitäisi olla ratkaisun avain, mutta toistaiseksi en ole saanut esimerkin lauseen tuottamaa bittisanakirjaa sopivaan muotoon.

> Mitä teen seuraavaksi?

Seuraavaksi jatkan Huffman-algoritmin viimeistelyä, sekä mahdollisimman pian aloitan opiskelemaan **LZ78** algoritmin toimintaa ja hahmottelemaan sitä osaksi projektia.

## Tuntikirjanpito

|PVM|Mitä tein?|Aikaa käytetty (h)|
|:--|:--|:--|
|12.9.|Binääridatan lukeminen ja kirjoittaminen Pythonilla|5|
|13.9.|Binääridatan lukeminen ja kirjoittaminen Pythonilla|4|
|16.9.|Binääridatan lukeminen ja kirjoittaminen Pythonilla|4|
|17.9.|CI-työkalun liittäminen projektiin, testien lisääminen, viikkoraportin kirjoittaminen|4|
|||yht. 17|
