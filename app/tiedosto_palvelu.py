import os


class TiedostoPalvelu:
    def __init__(self, tiedosto: str) -> None:
        """TiedostoPalvelu ottaa käsittelyyn annetun tiedoston.

        Annettu muuttuja 'tiedosto' voi olla absoluuttinen polku tiedostoon tai relatiivinen ajossa käytettyyn sijaintiin nähden.

        Args:
            tiedosto (str): Annetun tiedoston nimi tai sijainti ja nimi.
        """
        self.tiedosto = None
        self.on_tyhja_tiedosto = False
        if os.path.isfile(tiedosto):
            self.tiedosto = tiedosto
        if os.path.isfile(os.path.join(os.getcwd(), tiedosto)):
            self.tiedosto = os.path.join(os.getcwd(), tiedosto)
        if not self.tiedosto:
            self.on_tyhja_tiedosto = True
            self.tiedosto = tiedosto
        self.on_teksti_tiedosto = self._on_teksti_tiedosto()

    def lue_tiedosto(self):
        """Lue annetun tiedoston sisältö.

        Metodi olettaa .txt, .purettu, .c ja .lsp -päättellä olevien tiedostojen olevan tekstitiedostoja, muussa tapauksessa metodi pyrkii lukemaan tiedostoa binääritiedostona.

        Raises:
            OSError: Palautetaan virhe, jos yritetään lukea tyhjää tiedostoa.

        Returns:
            sisalto (str or bytearray): Palautetaan moodista riippuen sisältö tekstinä tai bittitaulukkona.
        """
        if self.on_tyhja_tiedosto:
            raise OSError("Yritetään lukea tyhjää tiedostoa")
        moodi = "r"
        if not self.on_teksti_tiedosto:
            moodi += "+b"

        with open(self.tiedosto, moodi) as luettava_tiedosto:
            sisalto = luettava_tiedosto.read()

        return sisalto

    def kirjoita_tiedosto(self, sisalto, moodi="w", algoritmi="lz") -> str:
        """Kirjoita tiedosto metodi ottaa annetun sisällön ja tallentaa sen tiedostoon.

        Args:
            sisalto (str or bytearray): Luettavan tiedoston sisältö.
            moodi (str, optional): Luettavan tiedoston lukemiseen käytettävä moodi, tekstille "w", binääridatalle "w+b". Oletuksena "w".
            algoritmi (str, optional): Käytetty algoritmi. Lisätään tunnisteena tiedostonimeen. Oletuksena "lz".

        Returns:
            tiedosto (str): Palautetaan kirjoitetun tiedoston polku
        """

        # print('moodi', moodi)
        # print(sisalto)
        # print(type(sisalto))
        # print(f'sisalto(bytearray): {isinstance(sisalto, bytearray)}')
        # print(f'sisalto(str): {isinstance(sisalto, str)}')

        if moodi == "w+b":
            if algoritmi == "huffman":
                self.tiedosto += ".huff"
            else:
                self.tiedosto += ".lz"
        else:
            self.tiedosto += ".purettu"
        with open(self.tiedosto, moodi) as tiedosto:
            if moodi == "w+b":
                tiedosto.write(bytearray(sisalto))
            else:
                tiedosto.write(sisalto)

        return self.tiedosto

    def _on_teksti_tiedosto(self):
        """Tarkistetaan tiedoston pääte, ja päätellään siitä onko kyseessä tekstitiedosto

        Returns:
                bool: Palauttaa True, jos annettu tiedoston pääte on '.txt'
        """
        return os.path.splitext(self.tiedosto)[1] in [".txt", ".purettu", ".c", ".lsp"]

    def __str__(self) -> str:
        return self.tiedosto
