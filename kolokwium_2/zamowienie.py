from dieta import Dieta
from osoba import Osoba
from pacjent import Pacjent
from dietetyk import Dietetyk


class Zamowienie:

    @property
    def id(self) -> int:
        return self._id

    @property
    def diety(self) -> list[Dieta]:
        return self._diety

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @property
    def dietetycy(self) -> list[Dietetyk]:
        return self._dietetycy

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @diety.setter
    def diety(self, value: list[Dieta]) -> None:
        self._diety = value

    @pacjent.setter
    def pacjent(self, value: Pacjent) -> None:
        self._pacjent = value

    @dietetycy.setter
    def dietetycy(self, value: list[Dietetyk]) -> None:
        self._dietetycy = value

    def wartosc(self) -> float:
        suma = 0
        for cena in self._diety:
            suma += cena.cena
        return f'Wartość zamówienia: {round(suma, 2)} zł'

    def sum_kcal(self) -> float:
        suma = 0
        for kcal in self._diety:
            suma += kcal.kcal
        return f'Łączna liczba kalorii: {round(suma, 2)} kcal'

    def __str__(self) -> str:
        return f'ID zamówienia: {self._id}, ' \
               f'diety {[str(i) for i in self._diety]} ' \
               f'{self._pacjent}, ' \
               f'dietetycy: {[str(d) for d in self._dietetycy]}'
