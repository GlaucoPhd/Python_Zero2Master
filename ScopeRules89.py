# Scope - what variables do I have access to?
# 1 Local Scope (a = 5 is the first variable of the local scope)
# 2 If there is nothing in the local scope
# 3 Global Scope
# 4 Built in python functions

a = 1
def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent())
print(a)
