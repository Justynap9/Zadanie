from Property import Property


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'House Data: area {self.area},' \
               f'plot {self.plot}, rooms {self.rooms},' \
               f'price {self.price}, address {self.address}.'
