from Shopping.Utility import muliply, divi
from Shopping.more_shopping import ShoppingCart
import random
print(ShoppingCart.buy('apple'))
print(divi(20, 5))
print(muliply(5, 3))
print(max(1, 2, 3))
print()

# Tip: __name__ == " File Name " run the code only in the file
print(__name__)
if __name__ == '__main__':
    print('Run This')

# Class created in the Main file
class Student():
    pass
st1 = Student()
print(type(st1))
#
# # Help function shows all the documentation for what it does.
help(random)
# # print(dir(random.)) "udr random. " show as all the methods we can process
print(dir(random))




