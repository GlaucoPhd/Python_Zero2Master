my_list = []
for char in 'hello':
    my_list.append(char)

print(my_list)

my_lista = {chara for chara in 'hello'}
my_listb = {num for num in range(0, 100)}
my_listc = {num*2 for num in range(0, 100)}
my_listd = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_lista)
print(my_listb)
print(my_listc)
print(my_listd)

simple_dict = {'a': 1, 'b': 2}
my_dict = {k: v**2 for k, v in simple_dict.items()}
print(my_dict)

simple_dicta = {'a': 1, 'b': 4}
my_dicta = {k: v**2 for k, v in simple_dicta.items() if v % 2 == 0}
print(my_dicta)

my_dictb = {num:num*2 for num in [1, 2, 3]}
print(my_dictb)
