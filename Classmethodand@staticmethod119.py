# @classmethod we dont need to instaciated


class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'My name is {self.name}.')

    @classmethod
    def adding_things(cls, numero1, numero2):
        return cls('Ted', numero1 + numero2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

print(PlayerCharacter.adding_things(2,3))
player1 = PlayerCharacter('Tom', 23)
print(player1.shout())
print(player1.adding_things(1, 3))




