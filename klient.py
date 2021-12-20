class Klient:
    def __init__(self, imie: str, nazwisko: str,
                 plec: str, ulica: str, miejscowosc: str) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._plec = plec
        self._ulica = ulica
        self._miejscowosc = miejscowosc

    @property
    def imie(self) -> str:
        return self._imie

    @imie.setter
    def imie(self, value: str) -> None:
        self._imie = value

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, value: str) -> None:
        self._nazwisko = value

    @property
    def plec(self) -> str:
        return self._plec

    @plec.setter
    def plec(self, value: str) -> None:
        self._plec = value

    @property
    def ulica(self) -> str:
        return self._ulica

    @ulica.setter
    def ulica(self, value: str) -> None:
        self._ulica = value

    @property
    def miejscowosc(self) -> str:
        return self._miejscowosc

    @miejscowosc.setter
    def miejscowosc(self, value: str) -> None:
        self._miejscowosc = value

    def __str__(self) -> str:
        return f'{self._imie} {self._nazwisko}, ' \
               f'miejsce zamieszkania: {self._ulica} {self._miejscowosc}'
