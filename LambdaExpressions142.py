from functools import reduce
my_list = [1,2,3]
def multiply2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))
print(my_list)
