# Data base collect user names, passwords and create new list

my_list = [1, 2, 3]
your_list = [10,20, 30]
their_list = [5, 4, 3]
def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list, your_list)))
print(list(zip(my_list, your_list, their_list)))
print(my_list)
