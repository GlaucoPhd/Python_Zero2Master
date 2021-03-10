class PlayCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('Run')

    def speak(self):
        print(f'Name {self.name}, and I am {self.age} years old')

player1 = PlayCharacter('andrei', 100)
player1.speak()
player2 = {'name': 'andrei', 'age': 100}
print(player2['name'])
print(player2['age'])


