# This examples last 2 print methods are out off the while loop...
# They appears only after the user input the right data type
# Finnally example cound be used in a game for track the users actions on it
print('1 - Example 1')
while True:
    try:
        age = int(input('What is your age: '))
        10 / age
    except ValueError:
        print('Letters are not allowed!Please enter a number now.')
        continue
    except ZeroDivisionError:
        print('Please enter a number higher than 0.')
    else:
        print('Thanks.')
        break


print('Ok, Finally Done.')
print('Are you there?\n')

print('2 - Example 2 - Finnaly runs until the end of the code dont matter what')

while True:
    try:
        age = int(input('What is your age: '))
        10 / age
    except ValueError:
        print('Letters are not allowed!Please enter a number now.')
        continue
    except ZeroDivisionError:
        print('Please enter a number higher than 0.')
    else:
        print('Thanks.')
        break
    finally:
        print('Ok, Finally Done.')
        print('Are you still there?')
