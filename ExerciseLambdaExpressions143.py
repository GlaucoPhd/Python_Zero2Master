my_list = [5, 4, 3]
def quadrada(item):
    return item**2


print(list(map(lambda item: item**2, my_list)))


# Teacher Organize a list by lowest second number

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)












