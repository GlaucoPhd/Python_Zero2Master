class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'name {self.name} and {self.age}')


player1 = PlayerCharacter('Andre', 12)
player1.speak()
player1.name = 'Roger'

print(player1.name)

