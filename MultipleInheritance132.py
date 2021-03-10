class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack ')

class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def check_arrow(self):
        print(f'arrowns left ')

    def run(self):
        print('Run really fast')

class Cyborg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrow)
        Wizard.__init__(self, name, power)
hb1 = Cyborg('Bor', 1)
print(hb1)
print(hb1.run)
