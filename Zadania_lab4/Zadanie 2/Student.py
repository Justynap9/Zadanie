class Student:
    def __init__(self, name, surname, street, city, zip_code, email):
        self.name = name
        self.surname = surname
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.email = email

    def __str__(self):
        return f'student: {self.name} {self.surname},' \
               f'residence: {self.street} {self.city}, {self.zip_code},' \
               f'email: {self.email}'
