from dieta import Dieta
from osoba import Osoba
from pacjent import Pacjent
from dietetyk import Dietetyk
from zamowienie import Zamowienie


dieta1 = Dieta('Fit', 1600, 'wegetariańska', 500)
dieta2 = Dieta('Sport', 2000, 'normalna', 700)
pacjent1 = Pacjent('pacjent', 'Ola', 'Nowak', '62762476', 32, 'Kobieta')
dietetyk1 = Dietetyk('Dietetyk', 'Anna', 'Kowalska',
                     '64773482', 'Diety wegetariańskie', '5 lat')
dietetyk2 = Dietetyk('Dietetyk', 'Michał', "Czapla",
                     '7758468', 'Dieta sportowa', '2 lata')
zamowienie1 = Zamowienie()
zamowienie1.id = 1
zamowienie1.diety = [dieta1, dieta2]
zamowienie1.pacjent = pacjent1
zamowienie1.dietetycy = [dietetyk1, dietetyk2]
print(zamowienie1.wartosc())
print(zamowienie1.sum_kcal())
print(zamowienie1)
