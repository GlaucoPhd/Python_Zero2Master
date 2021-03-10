# clean code
def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
print(is_odd_or_even(53))

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(23))

def is_odd(num):
    if num % 2 == 0:
        return True
    return False
print(is_odd(8))


def easy_even_odd(num):
    return num % 2 == 0

print(easy_even_odd(50))
