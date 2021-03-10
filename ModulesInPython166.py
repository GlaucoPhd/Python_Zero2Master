# 1 Example - First Way to import files to the active file
import Shopping.more_shopping.ShoppingCart
print(Shopping.more_shopping.ShoppingCart.buy('apple'))

# 2 Example - Also we can import only what functions we need (The best Way)
from Shopping.more_shopping.ShoppingCart import buy
print(buy('Pineaple'))

# 3 - Example 3 - From A import par_ou_impar

# 4 - Example - Also we can import everything - Its not a good practice
from A import *

def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print()
print(multiply(1, 31))
par_ou_impar(53)
p_ou_i(122)
