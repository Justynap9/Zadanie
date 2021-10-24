# Zadanie1

def welcome(name, surname: str) -> str:
    return (f'Cześć {name} {surname}!')

print(welcome('Anna', 'Kowalska'))

# Zadanie 2

def multiplication(x, y: int) -> int:
    return x*y

print(multiplication(12,12))

# Zadanie 3

def is_even(number) -> bool:
    return number % 2 == 0

result = is_even(2)
if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

# Zadanie 4

def sum(x, y, z: int) -> bool:
    return x + y >= z

print(sum(2,3,5))

# Zadanie 5

def is_contain(numbers: list, element: int):
    return element in numbers

print(is_contain([2,3,4,5], 6))

# Zadanie 6

def merge(list1, list2: list) -> list:
    list3 = list(set(list1 + list2))
    result = [i**3 for i in list3]
    return result

print(merge([1,2,3,3],[4,5,3,1]))


