# Fix we can use the try in a block indented
# While loop help get back to the beginning
# Eternal Loop
# a = ('1 - Example 1 infinite loop')
# print(a)
#
# while True:
#     try:
#         age = int(input('What is your age: '))
#         print(age)
#     except:
#         print('Please enter a number: ')

print('2 - Example 2 - Except, Else & Break fix infinite loop')
while True:
    try:
        age = int(input('What is your age? '))
        print(age)
    except:
        print('Please enter a number.')
    else:
        print('Thanks\n')
        break


print('3 - Example 3 - Valuerror, ')
while True:
    try:
        age = int(input('Age: '))
        10 / age
    except ValueError:
        print('Enter a number.')
    except ValueError:
        print('!!!')
    except ZeroDivisionError:
        print('Enter number higher them zero.')
    else:
        print('Thanks')
        break