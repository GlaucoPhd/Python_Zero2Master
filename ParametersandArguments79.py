# Def one function we can give paramethers inside of the parentheses.
# We can see to paramethers or variables that we created
# Use it dynamic

def say_hello(name, emoji):
	print(f'Helloooooooooooooo {name} {emoji}')
say_hello('Glauco', ':')

# Paramethers to define def say_hello(name, emoji)
# Arguments are used when we call a function


# Argument value pass into a function as input when we call the function
# We uses arguments so we can direct the function to do different kinds of work when call it al different times
# We put the arguments in parentheses after the name of the function
# big = max('Hello World')
#                 |-------------> Argument

# Parameters
# Is a variable wich we use in the function definition. Its a handle that allows the code in the function
# to access the arguments for a particular function invocation
# Def input data and return to output data

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bon Jour'
    else:
        return 'Hello'


print(greet('es'), 'Glenn')
print(greet('fr'), 'Sally')
print(greet('en'), 'Michael')

# Parameters without outputs
# def abc(las):
#     if langs == 'pt':
#         print('Oi')
#     elif langs == 'jp':
#         print('Sayonara')
#     else:
#         print('Noroc che ma fach')
# abc()