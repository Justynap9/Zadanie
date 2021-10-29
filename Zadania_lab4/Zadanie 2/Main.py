from Library import Library
from Order import Order
from Employee import Employee
from Book import Book
from Student import Student


library1 = Library("Katowice", "ul. Grunwaldzka 7", "40-004", "10:00 - 18:00", "659309945")
library2 = Library("Katowice", "ul. Polna 8", "40-000", "9:00-17:00", "567392009" )
employee1 = Employee("Adam", "Kowalski", "20-01-2005", "14-06-1980", "Katowice", "ul. 3 Maja 7/8", "40-067", "534890678")
employee2 = Employee("Aleksandra", "Nowak", "05-01-2010", "19-03-1990", "Katowice", "ul. De Gaulle'a 67", "40-067", "536789678")
employee3 = Employee("Piotr", "Wójcik", "25-01-2019", "22-10-1997", "Katowice", "ul. Królewska 7/8", "40-050", "968354719")
student1 = Student("Jan", "Drozd","ul. Wolności 23","Będzin","43-690","jandrozd@gmail.com")
student2 = Student("Natalia", "Kos","ul. Leśna 34", "Sosnowiec", "48-300", "nataliakos@gmail.com")
student3 = Student("Bożena", "Batory","ul. Warszawska 1","Częstochowa", "42-400","bożenabatory@gmail.com")
book1 = Book(library1,"Przeminęło z wiatrem", "1936", "Margharet", "Mitchell", '1056')
book2 = Book(library2,"Harry Potter i Insygnia Śmierci", "2007", "J.K", "Rowling", '784')
book3 = Book(library1,"Zabić drozda", "1960", "Harper", "Lee", '424')
book4 = Book(library1,"Python. Wprowadzenie", "2020", "Mark", "Lutz", '1496')
book5 = Book(library2,"Podstawy finansów", "2004", "Dorota", "Korenik", '233')
order1 = Order(employee1, student1, [book1,book2,book3],"23-09-2021")
order2 = Order(employee2, student3, [book4,book5], "13-07-2021")

print(order1)
print(order2)