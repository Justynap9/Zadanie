class Magazyn:
    def __init__(self, id: str, nazwa: str, ulica: str,
                 miejscowosc: str, kod_pocztowy: str) -> None:
        self._id = id
        self._nazwa = nazwa
        self._ulica = ulica
        self._miejscowosc = miejscowosc
        self._kod_pocztowy = kod_pocztowy

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value: str) -> None:
        self._nazwa = value

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

    @property
    def kod_pocztowy(self) -> str:
        return self._kod_pocztowy

    @kod_pocztowy.setter
    def kod_pocztowy(self, value: str) -> None:
        self._kod_pocztowy = value

    def __str__(self) -> str:
        return f'Magazyn id: {self._id}, nazwa: {self._nazwa},' \
               f'lokalizacja: {self._ulica} {self._miejscowosc}' \
               f'{self._kod_pocztowy}'
