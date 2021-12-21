class Dieta:
    def __init__(self, nazwa: str, kcal: float,
                 rodzaj: str, cena: float) -> None:
        self._nazwa = nazwa
        self._kcal = kcal
        self._rodzaj = rodzaj
        self._cena = cena

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def kcal(self) -> float:
        return self._kcal

    @property
    def rodzaj(self) -> str:
        return self._rodzaj

    @property
    def cena(self) -> float:
        return self._cena

    def __str__(self) -> str:
        return f'Dieta {self._nazwa}, zawiera {self._kcal} kcal ' \
               f'rodzaj: {self._rodzaj}, cena: {self._cena}'
