while True:
    try:
        age = int(input('Age: '))
        10 / age
    except ValueError:
        print('Enter a number.')
    except ZeroDivisionError:
        print('Enter number higher them zero.')
    else:
        print('Thanks')
        break
    finally:
        print('Done')


# https://docs.python.org/3/library/exceptions.html (Base classes exceptions)
# except TypeError as err helps peers
def sum(num1 , num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers {err}')

print(sum('1', 2))

print('2 Example 2 - Concatenate multiple errors')
def suma(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print('oooops :(, Try again')
        print(err)

print(suma(1, '2'))

print('3 Example 3 - Concatenate multiple errors')
