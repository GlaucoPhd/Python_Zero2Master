# Given the below class:
# My Solution

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('mauro', 14)
cat2 = Cat('roger', 1)
cat3 = Cat('Lia', 3)

def oldcat():
    cats = [cat1.age, cat2.age, cat3.age]
    a = max(cats)
    print(f'The oldest cat is {a} years old.')
print(oldcat())

# Teacher Solution


class Cater:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


def get_oldest_cat(*args):
    return max(args)


print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")