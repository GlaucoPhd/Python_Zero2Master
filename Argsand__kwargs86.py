# args ##kwargs
# Accept any numbers of characters is necessary
# Python Community Uses *args and **Kwargs
def super_func(*args):
    print(args)
    return sum(args)

# Rule of parameters: (params, **args, default parameters, **kwargs)
# Rule(name, *arg, i'', **kwargs)
def super_func_sum(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func_sum(1, 2, 3, num1=5, num=10))
