# Check Instance
class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attaking with arrows {self.arrows}')


wizard1 = Wizard('Glauco', 23)
archer1 = Archer('Davi', 5)

print('+-----------Wizard-----------+')
print(wizard1.sign_in())
print(wizard1.name)
wizard1.attack()
print('\n')

print('+-----------Archer-----------+')
print(archer1.sign_in())
print(archer1.name)
archer1.attack()
print('\n')

def player_attack(char):
    char.attack()

print('+-----------User player attack function-----------+')
print(player_attack(wizard1))
print(player_attack(archer1))

print('+-----------Check Isinstance-----------+')
print(isinstance(wizard1, object))

print('+-----------User player attack loop-----------+')
for char in [wizard1, archer1]:
    char.attack()

print(char.attack())
