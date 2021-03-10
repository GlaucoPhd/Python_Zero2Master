# Scope what variables do I have access to.
# Global Scope, anyway in this file or access to it can use it
# Functions defined by user, any function, variable its no avaliable to the file
def some_func():
    total = 100
    a = total + 10
    print(a)

print(some_func())