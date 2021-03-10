# no true private variables
# user _ to keep private variable
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'name {self._name} and {self._age}')


player1 = PlayerCharacter('Andre', 12)
player1.name = 'Roger'

print(player1.speak())

