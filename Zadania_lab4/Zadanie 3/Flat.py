from Property import Property


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Flat data: area {self.area},' \
               f'rooms {self.rooms}, floor {self.floor},' \
               f'price {self.price}, address {self.address}.'
