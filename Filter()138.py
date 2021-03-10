# Filter just get the result for for the items that matches with the code(in the code format)
# Map go all trough the list and return the boolean value for all items
my_list = [1, 2, 3]
def only_odd(item):
    return item % 2 != 0

print(list(map(only_odd, my_list)))
print(list(filter(only_odd, my_list)))
print(my_list)




