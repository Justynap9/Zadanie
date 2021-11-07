class Book:
    def __init__(self, library, title,
                 publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.title = title
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'{self.title}.' \
               f'Author: {self.author_name} {self.author_surname},' \
               f'number of pages:{self.number_of_pages},' \
               f'publication date:{self.publication_date}.' \
               f'Available in: {self.library}.'
