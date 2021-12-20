from magazyn import Magazyn
from klient import Klient
from produkt import Produkt


class Zamowienie():

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @property
    def produkt(self) -> list[Produkt]:
        return self._produkt

    @produkt.setter
    def produkt(self, value: list[Produkt]) -> None:
        self._produkt = value

    @property
    def klient(self) -> Klient:
        return self._klient

    @klient.setter
    def klient(self, value: Klient) -> None:
        self._klient = value

    @property
    def magazyn(self) -> Magazyn:
        return self._magazyn

    @magazyn.setter
    def magazyn(self, value: Magazyn) -> None:
        self._magazyn = value

    @property
    def ilosc(self) -> list[int]:
        return self._ilosc

    @ilosc.setter
    def ilosc(self, value: list[int]) -> None:
        self._ilosc = value

    def __str__(self) -> str:
        return f'Zamowienie id: {self._id}, klient: {self._klient},' \
               f'produkt: {self._produkt}, magazyn{self._magazyn},' \
               f'ilosc {self._ilosc}'

    def wartosc(self) -> float:
        suma = 0
        for i, p in enumerate(self.produkt):
            suma += p.cena * self.ilosc[i]
        return suma

    def adres(self) -> str:
        print(f'Adres: {self.klient.ulica} {self.klient.miejscowosc}')
