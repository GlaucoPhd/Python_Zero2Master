# Create a Class and identify the type of class
# Class BluePrint we want to create, basic atributes, methods,
# Intantiate a Class, create a Instance are (Objects)
# BigObject is the BluePrint
# obj1 = BigObject() Instanciate
# Inside the class insert the codd

class BigObject:
    pass

obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()


print(type(obj1))


class Glauco:
    def __init__(self, name):
        self.name = name
        print(name)


N1 = Glauco('H')
print(N1)



