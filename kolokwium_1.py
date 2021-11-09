class Klient:
    def __init__(self, imie: str, nazwisko: str, plec: str, ulica: str, miejscowosc: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._plec = plec
        self._ulica = ulica
        self._miejscowosc = miejscowosc 
    
    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def plec(self):
        return self._plec

    @property
    def ulica(self):
        return self._ulica

    @property
    def miejscowosc(self):
        return self._miejscowosc

    def __str__(self):
        return f'Klient: {self._imie} {self._nazwisko}, miejsce zamieszkania: {self._ulica} {self._miejscowosc}'

class KlientDetaliczny(Klient):
    def __init__(self, imie: str, nazwisko: str, plec: str, ulica: str, miejscowosc: str):
        super().__init__(imie, nazwisko, plec, ulica, miejscowosc)

     
    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def plec(self):
        return self._plec

    @property
    def ulica(self):
        return self._ulica

    @property
    def miejscowosc(self):
        return self._miejscowosc   

    def __str__(self):
        return f'Klient: {self._imie} {self._nazwisko}, miejsce zamieszkania: {self._ulica} {self._miejscowosc}'

class KlientBiznesowy(Klient):
    def __init__(self, imie: str, nazwisko: str, plec: str, ulica: str, miejscowosc: str, nazwa_firmy: str):
        super().__init__(imie, nazwisko, plec, ulica, miejscowosc)
        self._nazwa_firmy = nazwa_firmy

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def plec(self):
        return self._plec

    @property
    def ulica(self):
        return self._ulica

    @property
    def miejscowosc(self):
        return self._miejscowosc

    @property
    def nazwa_firmy(self):
        return self._nazwa_firmy

    def __str__(self):
        return f'Klient id: {self._id}, nazwa firmy: {self._nazwa_firmy}'

class KlientDetaliczny(Klient):
    def __init__(self, imie: str, nazwisko: str, plec: str, ulica: str, miejscowosc: str):
        super().__init__(imie, nazwisko, plec, ulica, miejscowosc)

     
    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def plec(self):
        return self._plec

    @property
    def ulica(self):
        return self._ulica

    @property
    def miejscowosc(self):
        return self._miejscowosc   
    
    def __str__(self):
        return f'Klient: {self._imie} {self._nazwisko}, miejsce zamieszkania: {self._ulica} {self._miejscowosc}'

class Produkt():
    def __init__(self, id: str, nazwa: str, kategoria: str, podkategoria: str, cena: float, ilosc: int):
        self._id = id
        self._nazwa = nazwa
        self._kategoria = kategoria
        self._podkategoria = podkategoria
        self._cena = cena
        self._ilosc = ilosc

    @property 
    def id(self):
        return self._id

    @property 
    def nazwa(self):
        return self._nazwa

    @property 
    def kategoria(self):
        return self._kategoria
    
    @property 
    def podkategoria(self):
        return self._podkategoria

    @property 
    def cena(self):
        return self._cena

    @property 
    def ilosc(self):
        return self._ilosc

    def __str__(self):
        return f'Produkt id: {self._id}, nazwa: {self._nazwa}, kategoria {self._kategoria}, podkategoria: {self._podkategoria}, cena: {self._cena}, ilosc: {self._ilosc}'

class Magazyn:
    def __init__(self, id: str, nazwa: str, ulica: str, miejscowosc: str, kod_pocztowy: str):
        self._id = id
        self._nazwa = nazwa
        self._ulica = ulica
        self._miejscowosc = miejscowosc
        self._kod_pocztowy = kod_pocztowy

    @property 
    def id(self):
        return self._id

    @property 
    def nazwa(self):
        return self._nazwa

    @property 
    def ulica(self):
        return self._ulica

    @property 
    def miejscowosc(self):
        return self._miejscowosc

    @property
    def kod_pocztowy(self):
        return self._kod_pocztowy

    def __str__(self):
        return f'Magazyn id: {self._id}, nazwa: {self._nazwa}, lokalizacja: {self._ulica} {self._miejscowosc} {self._kod_pocztowy}'
    

class Zamowienie():
    
    @property 
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def produkt(self):
        return self._produkt
    
    @produkt.setter
    def produkt(self, value: Produkt):
        self._produkt = value

    @property
    def klient(self):
        return self._klient

    @klient.setter
    def klient(self, value):
        self._klient = value

    @property
    def magazyn(self):
        return self._magazyn

    @magazyn.setter
    def magazyn(self, value: Magazyn):
        self._magazyn = value

    @property
    def ilosc(self):
        return self._ilosc

    @ilosc.setter
    def ilosc(self, value: int):
        self._ilosc = value


    
    def __str__(self):
        return f'Zamowienie id: {self._id}, klient: {self._klient}, produkt: {self._produkt}, magazyn{self._magazyn}, ilosc {self._ilosc}'
    

    def wartosc(self):
        cena = self._produkt._cena
        return cena * self.ilosc

    def adres(self):
        ulica = self._klient.ulica
        miejscowosc = self._klient.miejscowosc
        return f'Adres: {ulica} {miejscowosc}'


produkt1 = Produkt(1, 'a', 'b', 'c', 120.50, 2)
klient1 = Klient("Aleksandra", "Kowalska", "k", "ul. Sobieskiego 2/67", "Katowice")
magazyn1 = Magazyn("1", "Magazyn 1", "ul. Wierzbowa 2", "Warszawa", "20-000")
zamowienie1 = Zamowienie()
zamowienie1.id = "1"
zamowienie1.produkt = produkt1
zamowienie1.klient = klient1
zamowienie1.magazyn = magazyn1
zamowienie1.ilosc = 2
print(zamowienie1.produkt)
print(Zamowienie.wartosc(zamowienie1))
print(Zamowienie.adres(zamowienie1))
print(klient1)
print(magazyn1)
print(produkt1)
print(zamowienie1)

