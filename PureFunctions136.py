# Pure Function allways give the same result with the same input
# Function dont produce side effect
# Function Pure Example 1

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1, 2, 3]))

# Function Side Effect Example 2
def multiply_by3(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return print(new_list)

multiply_by3([1, 2, 3])

# Function Side Effect Example 3
new_list = []
def multiply_by4(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by4([1, 2, 3]))

# Function Side Effect Example 4 error because change to a string
new_list = []
def multiply_by5(li):
    for item in li:
        new_list.append(item*2)
    return new_list

new_list = ''
print(multiply_by5([1, 2, 3]))