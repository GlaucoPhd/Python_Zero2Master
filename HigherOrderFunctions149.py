# Hight Order Function HOC
# Function accept another function inside of his parameters
# @decorator
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func




