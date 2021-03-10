# Always class name singular
# __init__ Magic Method
# First Parameter when we write a code Class
# Define a self. only one user can be assigned to it
# Write code dynamic,
# Give a special attribute for a user only is available to him
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Glauco', 1)
player2 = PlayerCharacter('Thiago', 9)
player2.attack = 50

print(player1.name)
print(player2.age)
print(player2.attack)

print(player1)
