numbers1 = [4,5,6,7,8]

def numbers(list):
    list1 = []
    for i in list:
        list1 += [i*2]
    return list1

print(numbers(numbers1))
