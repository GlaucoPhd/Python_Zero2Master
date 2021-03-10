my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)

my_lista = [chara for chara in 'hello']
my_listb = [num for num in range(0, 100)]
my_listc = [num*2 for num in range(0, 100)]
my_listd = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_lista)
print(my_listb)
print(my_listc)
print(my_listd)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = [x for x in some_list if some_list.count(x) > 1]
print(duplicates)
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)


# dupclicates = [x for x in some_list if some_list.count(x)]
# print(dupclicates)
