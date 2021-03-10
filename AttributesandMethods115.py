# Membership class object attribute static

class PlayerCharacter:
    membership = True
    def __init__(self, name, age, classe):
        if (PlayerCharacter.membership):
            self.name = name
            self.age = age
            self.classe = classe

    def shout(self):
        print(f'I am {self.name}')
        return 'Done.'

    def run(self, hi):
        print(f'I am {self.name}')
        return 'Done.'


player1 = PlayerCharacter('Glauco', 34, 'Magician')
player2 = PlayerCharacter('Davi', 5, 'Warior')

player1.magic = 2003
player2.power = 100

print(player1.membership)
print(player2)

print(player1.classe)
print(player2.name, player2.power)

print(player1.shout())

