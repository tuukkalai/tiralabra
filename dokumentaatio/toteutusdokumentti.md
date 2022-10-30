# Toteutusdokumentti

## Ohjelman yleisrakenne

Rakenteeltaan ohjelma on pyritty pitämään yksinkertaisena erottamalla Huffman- ja LZ78-algoritmeja käyttävät pakkaus ja purku metodit omiin tiedostoihinsa, sekä erottamalla yhteisenä apukirjastona käytettävän `tiedosto_palvelu.py` -tiedoston. Tiedostoon `tiedosto_palvelu.py` on lisätty `TiedostoPalvelu`-luokka, joka tarjoaa tiedostojen lukemiseen ja kirjoittamiseen tarkoitetut metodit.

![Ohjelman rakenne](/dokumentaatio/kuvat/rakenne.png "Ohjelman rakenne")

## Pseudokoodi

### Huffman

#### Pakkaaminen

```py
pakkaa(tiedosto):
    merkkien_esiintyvyys = esiintyvyys_laskin(tiedosto)
    sanakirja = huffman_puu(merkkien_esiintyvyys)
    pakattu_sisalto = yhdista_teksti_ja_sanakirja(tiedosto, sanakirja)
    kirjoita_tiedosto(pakattu_sisalto)
```

```py
esiintyvyys_laskin(tiedosto):
    sanakirja = {}
    for kirjain in tiedosto:
        if kirjain in sanakirja:
            sanakirja[kirjain] += 1
        else:
            sanakirja[kirjain] = 1
    return sanakirja järjestettynä suurimmasta pienimpään # Timsort, aika: O(n log n), tila: O(n)
```

```py
huffman_puu(sanakirja):
    while len(sanakirja) > 1:
        yhdistä kaksi vähiten esiintyvää merkkiä solmuksi
        järjestä sanakirja # Timsort, aika: O(n log n), tila: O(n)
    return huffman_binaari(juurisolmu)
```

```py
huffman_binaari(solmu, binääriesitys):
    if solmu == lehti:
        lisää merkki ja binääriesitys taulukkoon 
    huffman_binaari(solmun vasen lapsi, binääriesitys+'0')  # aika: O(n)
    huffman_binaari(solmun oikea lapsi, binääriesitys+'1')  # aika: O(n)
    return merkkien binääriesitykset taulukoituna
```

```py
yhdista_teksti_ja_sanakirja(tiedosto, sanakirja):
    palautettava = otsaketiedot
    palautettava += sanakirja
    for merkki in tiedosto: # aika: O(n)
        palautettava += sanakirja[merkki] 
    return palautettava
```

#### Purkaminen

```py
pura(tiedosto):
    tiedosto_sisalto = lue_tiedosto(tiedosto)
    sisalto_binaari = levitä tavutettu tiedosto merkkijonoksi ykkösiä ja nollia

    # Ensimmäiset 2 tavua sisältää sanakirjan pituuden
    sanakirjan_pituus = ota (pop) sisalto_binaari[:16]
    # Seuraavat 3 bittiä kertovat lopussa olevien ylimääräisten bittien määrän
    ylimääräiset_bitit = ota (pop) sisalto_binaari[:3]

    # Luodaan uudelleen sanakirja Postorder traversal-algoritmilla
    i = 0
    apumuuttuja = ''
    while i < sanakirjan_pituus:
        if sisalto_binaari[i] == '0':
            apumuuttuja += '0'
            i += 1
        else:
            merkki = sisalto_binaari[i+1:i+8]
            sanakirja[merkki] = apumuuttuja
            if len(apumuuttuja) > 0 and apumuuttujan lopussa on ykkösiä: # ollaan käyty haaran oikeanpuoleinen lapsi
                # Poistetaan viimeinen ykkönen
                apumuuttuja = apumuuttuja[:-1]
            # Poistetaan viimeinen nolla, korvataan ykkösellä
            apumuuttuja = apumuuttuja[:-1] + '1'
            i += 9 # kasvatetaan indeksiä luetun indeksin ja merkin verran

    # Dekoodataan pakattu teksti (sanakirjan lopun ja ylimääräisten bittien välistä) lisäämällä sanakirjasta löytyvä vastine muuttujaan dekoodattu teksti
    dekoodattu_teksti = ''
    apumuuttuja = ''
    for bitti in sisalto_binaari[sanakirjan_pituus:-ylimääräiset_bitit]:
        apumuuttuja += bitti
        if bitti in sanakirja:
            dekoodattu_teksti.append()
            apumuuttuja = ''

    kirjoita_tiedostoon(dekoodattu_teksti)
```

### LZ78

#### Pakkaaminen

```py
pakkaa(tiedosto):
    tiedosto_sisalto = lue_tiedosto(tiedosto)
    for merkki in tiedosto_sisalto: # O(n)
        apumuuttuja += merkki
        if apumuuttuja not in sanakirja:
            lisää apumuuttuja sanakirjaan
            # Jos tuntematon merkkijono ilman viimestä merkkiä on tunnettu (löytyy sanakirjasta) ->
            # lisätään viittaus tunnettuun merkkijonoon tuntemattoman merkkijonon indeksiin sijaintilistaan
            lisää apumuuttuja[:-1] sijainti sijaintilistaan
            apumuuttuja = ''
    
    # Tehdään binääri-muotoinen esitys sijainneista ja seuraavista merkeistä
    binaari = ''
    for sijainti in sijaintilista:
        binaari += enkoodataan sijainti mahdollisimman lyhyen esitysmuodon mukaan
        binaari += sijaintia seuraava merkki

    tavut = []
    for tavu in binaari:
        lisätään binääriesitys tavutettuna listaan
        if viimeinen tavu on lyhyempi kuin 8 merkkiä:
            lisätään loppuun nollia täyttämään tyhjä tila

    kirjoita_tiedostoon(tavutettu binääriesitys)
```

#### Purkaminen

```py
pura(tiedosto):
    tiedosto_sisalto = lue_tiedosto(tiedosto)
    sisalto_binaari = levitä tavutettu tiedosto merkkijonoksi ykkösiä ja nollia
    i = 0
    while len(sisalto_binaari) > 0:
        i % 2 == 0:
            sijainti = ota (pop) sijaintia vastaavat merkit
            kirjain = ota (pop) sijaintia seuraava tavu
            if sijainti == 0:
                sanakirja.append(kirjain)
            else:
                sanakirja.append( sanakirja[sijainti] + kirjain )
        i += 1
    
    teksti = yhdistä sanakirjan merkit ja merkkijonot jonoksi
    kirjoita_tiedostoon(teksti)
```

## Suorituskykyvertailu

### Huffman

```txt
Tekstitiedostojen pakkaaminen Huffman-algoritmia käyttäen

Tiedosto                                Koko alkuperäisestä      Aikaa käytetty      
sia_cheap_thrills.txt.huff              59.21 %                  3.01 ms             
jfk_virkaanastujaispuhe.txt.huff        55.28 %                  7.88 ms             
simple_test.txt.huff                    37.10 %                  0.29 ms             
fields.c.huff                           64.04 %                  6.63 ms             
grammar.lsp.huff                        60.95 %                  2.26 ms             
lcet10.txt.huff                         57.17 %                  168.26 ms           
alice29.txt.huff                        55.65 %                  65.43 ms            
asyoulik.txt.huff                       60.63 %                  51.71 ms            
plrabn12.txt.huff                       55.26 %                  181.10 ms           

---

Tekstitiedostojen purkaminen Huffman-algoritmia käyttäen

Tiedosto                                Aikaa käytetty      
jfk_virkaanastujaispuhe.txt.huff.purettu48.15 ms            
sia_cheap_thrills.txt.huff.purettu      18.41 ms            
simple_test.txt.huff.purettu            0.26 ms             
plrabn12.txt.huff.purettu               4119.47 ms          
fields.c.huff.purettu                   132.11 ms           
alice29.txt.huff.purettu                1197.77 ms          
grammar.lsp.huff.purettu                31.58 ms            
asyoulik.txt.huff.purettu               1031.46 ms          
lcet10.txt.huff.purettu                 3769.72 ms
```

### LZ78

```txt
Tekstitiedostojen pakkaaminen LZ78-algoritmia käyttäen

Tiedosto                                Koko alkuperäisestä      Aikaa käytetty      
sia_cheap_thrills.txt.lz                65.61 %                  5.46 ms             
jfk_virkaanastujaispuhe.txt.lz          64.90 %                  12.93 ms            
simple_test.txt.lz                      62.90 %                  0.31 ms             
fields.c.lz                             57.87 %                  17.59 ms            
grammar.lsp.lz                          61.52 %                  6.05 ms             
lcet10.txt.lz                           48.24 %                  547.53 ms           
alice29.txt.lz                          51.61 %                  178.66 ms           
asyoulik.txt.lz                         55.50 %                  144.58 ms           
plrabn12.txt.lz                         51.14 %                  575.94 ms           

---

Tekstitiedostojen purkaminen LZ78-algoritmia käyttäen

Tiedosto                                Aikaa käytetty      
sia_cheap_thrills.txt.lz.purettu        4.70 ms             
jfk_virkaanastujaispuhe.txt.lz.purettu  13.18 ms            
simple_test.txt.lz.purettu              0.34 ms             
asyoulik.txt.lz.purettu                 767.58 ms           
fields.c.lz.purettu                     18.42 ms            
alice29.txt.lz.purettu                  1171.92 ms          
plrabn12.txt.lz.purettu                 20131.32 ms         
lcet10.txt.lz.purettu                   15156.83 ms         
grammar.lsp.lz.purettu                  5.82 ms
```

## Työn mahdolliset puutteet ja parannusehdotukset

- Totetutetut algoritmit toimivat vain ASCII-muodossa olevien tekstitiedostojen kanssa -> Tuki UTF-8 tiedostoille.
- Tiedostojen käsittelyyn on lisätty kovakoodattuna joitain toimivaksi todettuja tiedostotyyppejä -> Tuki kaikille tekstityypeille.
- Joissain tapauksissa Huffman-algoritmi lisää loppuun ylimääräisen merkin. -> Lisää selvitystä
- LZ78 sanakirjan rajoitteena on sijaintien määrä (2^16), suuremmilla tiedostoilla ei toimi. -> Dynaaminen sanakirjan koon määrittäminen.
- Sovellukset ajetaan komennolla `python app/...` projektin juurihakemistosta -> ajettava shell komento?

## Lähteet

["Sophomore College - CS 10SC. Intellectual Excitement of Computer Science" student projects "Data Compression". Eric Roberts, Stanford University. 2000-2001](https://cs.stanford.edu/people/eroberts/courses/soco/projects/data-compression/datacompress.html)

[Calgary corpus](https://en.wikipedia.org/wiki/Calgary_corpus)

["Calgary corpus". Matt Powell, University of Canterbury. Viimeksi päivitetty 8 Tammikuuta, 2001](https://corpus.canterbury.ac.nz/descriptions/#calgary)

[Canterbury corpus](https://en.wikipedia.org/wiki/Canterbury_corpus)

[Kurt McMahon's "CSCI 241: Intermediate Programming in C++"](https://faculty.cs.niu.edu/~mcmahon/CS241/Notes/Data_Structures/binary_tree_traversals.html)

[Efficient way of storing Huffman tree - Stack Overflow](https://stackoverflow.com/questions/759707/efficient-way-of-storing-huffman-tree)

[Michel Goemans, Lempel-Ziv codes 18.310A lecture notes, April 27, 2015](https://math.mit.edu/~goemans/18310S15/lempel-ziv-notes.pdf)

