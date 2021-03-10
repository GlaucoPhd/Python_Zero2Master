# Create Counter get a global variable value

# The error is because dont refer to the variable outside

# def count():
#     total += 1
#     return total
#
# count()
total = 0
def count():
    total = 0
    total += 1
    return total

# Every time run a function reset the function value
# Global gets confusion every time the code is getting bigger and more complex

print(count())


totals = 0

def count_global():
    global totals
    totals += 2
    return totals

print(count_global())

# Insert paramether in the function

totalx = 0
def count_globals(totalx):
    totalx += 4
    return totalx
print(count_globals(5))




