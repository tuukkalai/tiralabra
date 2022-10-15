import os


class TiedostoPalvelu:
    def __init__(self, tiedosto: str) -> None:
        print("tiedosto", tiedosto)
        self.tiedosto = None
        if os.path.isfile(tiedosto):
            self.tiedosto = tiedosto
        if os.path.isfile(os.path.join(os.getcwd(), tiedosto)):
            self.tiedosto = os.path.join(os.getcwd(), tiedosto)
        print("self.tiedosto", self.tiedosto)
        if not self.tiedosto:
            raise OSError("Tiedostoa ei löydy")
        self.on_teksti_tiedosto = self._on_teksti_tiedosto()
        print("self.on_teksti_tiedosto", self.on_teksti_tiedosto)

    def lue_tiedosto(self) -> str:
        moodi = "r"
        if not self.on_teksti_tiedosto:
            moodi += "+b"

        with open(self.tiedosto, moodi) as luettava_tiedosto:
            sisalto = luettava_tiedosto.read()

        return sisalto

    def _on_teksti_tiedosto(self):
        """Tarkistetaan tiedoston pääte, ja päätellään siitä onko kyseessä tekstitiedosto

        Returns:
                bool: Palauttaa True, jos annettu tiedoston pääte on '.txt'
        """
        return os.path.splitext(self.tiedosto)[1] == ".txt"

    def __str__(self) -> str:
        return self.tiedosto
