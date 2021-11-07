class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Property data: area {self.area},' \
               f'rooms {self.rooms}, price {self.price},' \
               f'address {self.address}.'
