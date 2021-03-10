# Fibonacci
import fn as fn


F1 = 1
Fn = Fn - 1 + Fn - 2
F1 = 1, F2 = 1

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
for x in fib(21):
    print(x)

print('2 Example - List')

def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(10000))