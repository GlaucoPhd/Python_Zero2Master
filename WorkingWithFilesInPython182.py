# Read open function only read the file once
# 1 - Example 1 -  Read only Once
my_file = open('Text.txt')
print(my_file.read())
print(my_file.read())
print(my_file.read())

# 2 - Example 2 -  Read everytime
my_file.seek(0)
print(my_file.read())

# 3 - Examle 3 - Read a specific line
my_file.seek(0)
print(my_file.readline())

# 4 - Examle 4 - Read a list, separate \n indicate new lines
my_file.seek(0)
print(my_file.readlines())

# 5 - Example 5 - Need to close the file
my_file.close()


