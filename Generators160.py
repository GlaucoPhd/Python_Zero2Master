# Iterable any object we can loop to  __iter__
# Iterate act to use the itreable to process
# Generators range it is  one . List() are note
# Yield we dont store the value in memory

print('1 - Example 1 - Store Value in List')

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(15)
print(list(range(6)))

print('2 - Example 2 - Dont Store the Value')
def generator_function():
    for i in range(5):
        yield i*2
for item in generator_function():
    print(item)


print('3 - Example 3 - Yield keyword pauses the function, Next come back to the function ')

def generator_num(num):
    for i in range(num):
        yield i*2

g = generator_num(100)
next(g)
next(g)
print(next(g))
