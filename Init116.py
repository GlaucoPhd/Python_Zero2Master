class PlayerCharacter:
    membership = True

    def __init__(self, name='anonimo', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'Name is {self.name}')

player1 = PlayerCharacter('tome', 19)
print(player1.shout())


