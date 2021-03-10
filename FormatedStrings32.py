#Formated strings

name = 'Glauco'
age = 55
print('Hi ' + name + '. You are ' + str(age) + ' years old')
print(f'Hi {name}. You are {age} years old')
print('Hi {}. You are {} years old.'.format('Cial', '2'))
print('Hi {0}. You are {1} years old.'.format(name, age))
print('Hi {new_name}. You are {age} years old.'.format(new_name='Davi', age=23))
