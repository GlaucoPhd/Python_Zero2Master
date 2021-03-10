# @my_decorator main function can call the my_decorator function
# despiste we have a lot of my_decorator we assign to a specific one
# 🤖
print('1 - Example 1')
def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********\n')
    return wrap_func

@my_decorator
def hello():
    print('helloooooo')

@my_decorator
def bye():
    print('see yah')

hello()

print('2 - Example 2')
def my_decorator(funck):
    def wrap_funck():
        print('*********')
        funck()
        print('*********\n')
    return wrap_funck

@my_decorator
def hello_a():
    print('hellloss')

@my_decorator
def bye_a():
    print('hih')

hello_a()

print('3 - Example 3')
def my_decorator(funcky):
    def wrap_funcky(x):
        print('*********')
        funcky(x)
        print('*********\n')
    return wrap_funcky

@my_decorator
def hello_b(greet):
    print(greet)

@my_decorator
def bye_b():
    print('Good Bye')

hello_b('x')

print('4 - Example 4 a With paramether')
def my_decorator(funcky):
    def wrap_funcky(x):
        print('*********')
        funcky(x)
        print('*********')
    return wrap_funcky

@my_decorator
def hello_b(greet):
    print(greet)

@my_decorator
def bye_b():
    print('Good Bye')

hello_b('x')

print('5 - Example 5 More then 1 parameter')
def my_decorator(funckw):
    def wrap_funckw(*args, **kwargs):
        print('*********')
        funckw(*args, **kwargs)
        print('*********')
    return wrap_funckw

@my_decorator
def hello_c(greeting, emoji=':)'):
    print(greeting, emoji)

@my_decorator
def bye_c():
    print('Bye Bye')

hello_c('x', '🤖')

