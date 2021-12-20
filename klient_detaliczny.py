from klient import Klient


class KlientDetaliczny(Klient):
    def __init__(self, imie: str, nazwisko: str, plec: str,
                 ulica: str, miejscowosc: str, telefon: str) -> None:
        super().__init__(imie, nazwisko, plec, ulica, miejscowosc)
        self._telefon = telefon

    @property
    def telefon(self) -> str:
        return self._telefon

    @telefon.setter
    def telefon(self, value: str) -> None:
        self._telefon = value

    def __str__(self) -> str:
        return f'Klient: {self._imie} {self._nazwisko},' \
               f'miejsce zamieszkania: {self._ulica} {self._miejscowosc}'
