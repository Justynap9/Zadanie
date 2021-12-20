from klient import Klient


class KlientBiznesowy(Klient):
    def __init__(self, imie: str, nazwisko: str, plec: str,
                 ulica: str, miejscowosc: str, nazwa_firmy: str) -> None:
        super().__init__(imie, nazwisko, plec, ulica, miejscowosc)
        self._nazwa_firmy = nazwa_firmy

    @property
    def nazwa_firmy(self) -> str:
        return self._nazwa_firmy

    @nazwa_firmy.setter
    def nazwa_firmy(self, value: str) -> None:
        self._nazwa_firmy = value

    def __str__(self) -> str:
        return f'Nazwa firmy: {self._nazwa_firmy}'
