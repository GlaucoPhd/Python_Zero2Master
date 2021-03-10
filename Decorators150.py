# Decorator is a function that wrap doesnt change anything
# Benefit is we can enhance our function add functionalyties
def my_decorator(func):
    def wrap_func():
        print('*************')
        func()
        print('*************')
    return wrap_func()


@my_decorator
def hello():
    print('helllooooo')


def bye():
    print('see yah')


bye()


@my_decorator
def man():
    print('Oh Man')


man()
