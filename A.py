# clean code
print('--- Example 1 ---')

def par_ou_impar(num):
    if num % 2 == 0:
        return 'par'
    if num % 2 != 0:
        return 'impar'


print(f'O número é {par_ou_impar(12)}\n')
print('--- Example 2 ---')


def p_ou_i(nume):
    if nume % 2 == 0:
        return True
    if nume % 2 != 0:
        return False


print(f'Even or odd number result is: {p_ou_i(11)}\n')
print('--- Example 3 Teacher ---')


def is_odd_or_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


print(is_odd_or_even(53), '\n')
print('--- Example 4 - Clean VS1 ---')


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(23), '\n')


print('--- Example 4 - Clean VS1 ---')
def impar(num):
    if num % 2 != 0:
        return True
    else:
        return False


print(impar(2),'\n')
print('-> Example 5 Clean V2 \n')


def par(num):
    if num % 2 != 0:
        return True
    else:
        return False


print(par(2))
print('--- Example 6 - Clean code ---')


def is_odd(num):
    if num % 2 == 0:
        return True
    return False


print(is_odd(8), '\n')


print('--- Example 7 - Clean code ---')


def easy_even_odd(num):
    return num % 2 == 0


print(easy_even_odd(50))


print('--- Example 8 - Clean code ---')
def cl(num):
    return num % 2 == 0


print(cl(1),'\n')

def clean(num):
    if num % 2 == 0:
        return True

print(f'É {clean(2)}')
