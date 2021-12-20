from produkt import Produkt
from zamowienie import Zamowienie
from magazyn import Magazyn
from klient import Klient
from klient_detaliczny import KlientDetaliczny
from klient_biznesowy import KlientBiznesowy

produkt1 = Produkt(1, 'a', 'b', 'c', 120.50, 2)
produkt2 = Produkt(2, 'b', 'c', 'd', 10.50, 10)
klient1 = Klient("Aleksandra", "Kowalska", "k",
                 "ul. Sobieskiego 2/67", "Katowice")
magazyn1 = Magazyn("1", "Magazyn 1", "ul. Wierzbowa 2", "Warszawa", "20-000")
zamowienie1 = Zamowienie()
zamowienie1.id = "1"
zamowienie1.produkt = [produkt1, produkt2]
zamowienie1.klient = klient1
zamowienie1.magazyn = magazyn1
zamowienie1.ilosc = [2, 3]
print(zamowienie1.wartosc())
zamowienie1.adres()
print(zamowienie1)
