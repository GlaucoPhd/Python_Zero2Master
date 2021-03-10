# 1 Example - Create a variable name, also dont need to close the file
with open('Text.txt') as my_file:
    print(my_file.readlines())

# 2 Example - Open has one paramether called
with open('Text.txt', mode='r') as meu:
    print(meu.readlines())

# # 2 Example - Open has one paramether read and write erase the text
# with open('Text.txt', mode='r+') as my_file:
#     print(my_file.readlines())

