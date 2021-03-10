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

print(wizard1.sign_in())
print(wizard1.name)
wizard1.attack()

print(archer1.sign_in())
print(archer1.name)
archer1.attack()

