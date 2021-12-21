from osoba import Osoba


class Dietetyk(Osoba):
    def __init__(self, kategoria: str, imie: str,
                 nazwisko: str, telefon: str, specjalizacja: str,
                 staz_pracy: str) -> None:
        super().__init__(kategoria, imie, nazwisko, telefon)
        self._specjalizacja = specjalizacja
        self._staz_pracy = staz_pracy

    @property
    def specjalizacja(self) -> str:
        return self._specjalizacja

    @property
    def staz_pracy(self) -> str:
        return self._staz_pracy

    def __str__(self) -> str:
        return f'Kategoria: {self._kategoria}, imię {self._imie} ' \
               f'nazwisko: {self._nazwisko}, kontakt: {self._telefon} ' \
               f'specjalizacja: {self._specjalizacja}, ' \
               f'staż pracy: {self._staz_pracy}'
