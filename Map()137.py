# Map, Filter, zip and reduce
# Map call the function, we dont need the parentheses
# Loop each item
# Return the effect we want

# Example 1 (No side effect)
my_list = [1, 2, 3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1, 2, 3])))



def only_odd(item):
    return item % 2 != 0


# Example 2 (No side effect)
my_list = [1, 2, 3]
def multiply_by3(item):
    return item*2

print(list(map(multiply_by3, my_list)))
print(my_list)

my_list = ['jk', 'qew', 'eer']
def multiply_by4(item):
    return item

print(list(map(multiply_by4, my_list[0].upper())))






