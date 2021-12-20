class Produkt():
    def __init__(self, id: str, nazwa: str, kategoria: str,
                 podkategoria: str, cena: float, ilosc: int) -> None:
        self._id = id
        self._nazwa = nazwa
        self._kategoria = kategoria
        self._podkategoria = podkategoria
        self._cena = cena
        self._ilosc = ilosc

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
    def kategoria(self) -> str:
        return self._kategoria

    @kategoria.setter
    def kategoria(self, value: str) -> None:
        self._kategoria = value

    @property
    def podkategoria(self) -> str:
        return self._podkategoria

    @podkategoria.setter
    def podkategoria(self, value: str) -> None:
        self._podkategoria = value

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, value: float) -> None:
        self._cena = value

    @property
    def ilosc(self) -> int:
        return self._ilosc

    @ilosc.setter
    def ilosc(self, value: int) -> None:
        self._ilosc = value

    def __str__(self) -> str:
        return f'Produkt id: {self._id}, nazwa: {self._nazwa}, '\
               f'kategoria {self._kategoria}, podkategoria: '\
               f'{self._podkategoria}, '\
               f'cena: {self._cena}, stan magazynu: {self._ilosc}'
