# Määrittelydokumentti

> Mitä ohjelmointikieltä käytät? Kerro myös mitä muita kieliä hallitset siinä määrin, että pystyt tarvittaessa vertaisarvioimaan niillä tehtyjä projekteja.

Projektissa aion käyttää *Python*ia.

Muita kieliä, joita hallitsen vertaisarvioinnin vaatiman määrän, ovat *Java* ja *JavaScript*.

> Mitä algoritmeja ja tietorakenteita toteutat työssäsi?
> Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet?

Projektissa aion tutkia häviöttämiä pakkausalgoritmeja (*Huffman* ja *LZ78*) ja niiden käyttämiä tietorakenteita:

- avain-arvo parien listan esittäminen Pythonin sanakirjana `dict`

Tarkoituksena on tehdä komentoriviltä toimivat Huffman- ja Lempel-Ziv pakkausalgoritmejä noudattavat ohjelmat ja vertailla niiden ominaisuuksia.

> Mitä syötteitä ohjelma saa ja miten näitä käytetään?

Syötteinä ohjelmille voidaan antaa tekstimuotoista dataa. Ottaakseni huomioon eri kielien eroja, käytän suomenkielisen tekstin (esim. Kalevala) lisäksi [Calgary corpus](https://en.wikipedia.org/wiki/Calgary_corpus) -kokoelmaa, joka on luotu juuri pakkausalgoritmien vertailua varten.

> Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)

Pakkausalgoritmeillä pyritään pienentämään tiedoston vaatiman tilan määrä, ja [kurssin aiheiden](https://tiralabra.github.io/2022_p1/fi/aiheet/) pohjalta suositeltiin pakkausalgoritmien pakkaavan testitiedosto 40-60% alkuperäistä pienemmäksi.

Alkuperäisen selvitystyön perusteella arvioisin järkeväksi algoritmien aika- ja tilavaativuuksien tavoitteeksi iso-O notaatiolla luokan *O(n)*.

> Lähteet

["Sophomore College - CS 10SC. Intellectual Excitement of Computer Science" student projects "Data Compression". Eric Roberts, Stanford University. 2000-2001](https://cs.stanford.edu/people/eroberts/courses/soco/projects/data-compression/datacompress.html)

["Calgary corpus". Matt Powell, University of Canterbury. Viimeksi päivitetty 8 Tammikuuta, 2001](https://corpus.canterbury.ac.nz/descriptions/#calgary)

> Kurssin hallintaan liittyvät

Tietojenkäsittelytieteen kandidaatti (TKT)

Projektin koodissa, kommenteissa ja dokumentaatiossa käytetty kieli: suomi
