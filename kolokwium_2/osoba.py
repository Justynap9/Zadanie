class Osoba:
    def __init__(self, kategoria: str, imie: str,
                 nazwisko: str, telefon: str) -> None:
        self._kategoria = kategoria
        self._imie = imie
        self._nazwisko = nazwisko
        self._telefon = telefon

    @property
    def kategoria(self) -> str:
        return self._kategoria

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def telefon(self) -> str:
        return self._telefon

    def __str__(self) -> str:
        return f'Kategoria: {self._kategoria}, imię {self._imie} ' \
               f'nazwisko: {self._nazwisko}, kontakt: {self._telefon}'
