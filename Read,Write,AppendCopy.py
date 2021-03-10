# 1 Example - Wrote on the file (see the numbers of characters)
with open('Text2.txt', mode='w') as meu_arquivo:
    text = meu_arquivo.write('Glaucooo')
    print(text)

# 2 Example - Open use the append mode put at the and of the file
with open('Texto3.txt', mode='a') as arquivo:
    texto = arquivo.write(':)')
    print(texto)

# 3 Example - Create a file
with open('Text5.txt', mode='a') as hoje:
    texto = hoje.write('New')
    print(texto)




# # 2 Example - Open has one paramether read and write erase the text
# with open('Text.txt', mode='r+') as my_file:
#     print(my_file.readlines())

