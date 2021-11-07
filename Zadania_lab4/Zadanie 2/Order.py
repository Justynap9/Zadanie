class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Order placed by {self.student},' \
               f'order_date: {self.order_date},' \
               f'borrowed books: {[str (i) for i in self.books]}.' \
               f'Order executed by {self.employee}'
