from osoba import Osoba


class Pacjent(Osoba):
    def __init__(self, kategoria: str, imie: str,
                 nazwisko: str, telefon: str, wiek: int, plec: str) -> None:
        super().__init__(kategoria, imie, nazwisko, telefon)
        self._wiek = wiek
        self._plec = plec

    @property
    def wiek(self) -> int:
        return self._wiek

    @property
    def plec(self) -> str:
        return self._plec

    def __str__(self) -> str:
        return f'Kategoria: {self._kategoria}, imię {self._imie} ' \
               f'nazwisko: {self._nazwisko}, kontakt: {self._telefon} ' \
               f'wiek: {self._wiek}, płeć: {self._plec}'
