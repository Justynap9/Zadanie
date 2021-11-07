def numbers(list1):
    for i in range(len(list1)):
        list1[i] *= 2
    return list1


numbers1 = [4, 5, 6, 7, 8]
print(numbers(numbers1))
