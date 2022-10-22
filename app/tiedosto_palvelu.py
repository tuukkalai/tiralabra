import os


class TiedostoPalvelu:
    def __init__(self, tiedosto: str) -> None:
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
        if self.on_tyhja_tiedosto:
            raise OSError("Yritetään lukea tyhjää tiedostoa")
        moodi = "r"
        if not self.on_teksti_tiedosto:
            moodi += "+b"

        with open(self.tiedosto, moodi) as luettava_tiedosto:
            sisalto = luettava_tiedosto.read()

        return sisalto

    def kirjoita_tiedosto(self, sisalto, moodi='w'):
        # print('moodi', moodi)
        # print(sisalto)
        # print(type(sisalto))
        # print(f'sisalto(bytearray): {isinstance(sisalto, bytearray)}')
        # print(f'sisalto(str): {isinstance(sisalto, str)}')
        if moodi == 'w+b':
            self.tiedosto += '.lz'
        else:
            self.tiedosto += '.purettu'
        with open(self.tiedosto, moodi) as tiedosto:
            if moodi == 'w+b':
                tiedosto.write(bytearray(sisalto))
            else:
                tiedosto.write(sisalto)
        
        return self.tiedosto


    def _on_teksti_tiedosto(self):
        """Tarkistetaan tiedoston pääte, ja päätellään siitä onko kyseessä tekstitiedosto

        Returns:
                bool: Palauttaa True, jos annettu tiedoston pääte on '.txt'
        """
        return os.path.splitext(self.tiedosto)[1] in [".txt", ".purettu"]

    def __str__(self) -> str:
        return self.tiedosto
