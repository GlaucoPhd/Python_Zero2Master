# Regular Expression Boolean return str in item
# Span where its happen. End where its finish
# Group(0)
# Compile
import re

pattern = re.compile('meu')
linha = 'Vamos meu amigo meu tempo está acabando.'
print('meu' in linha)

m = re.search('meu', linha)
a = pattern.search(linha)
b = pattern.findall(linha)
c = pattern.fullmatch(linha)
d = pattern.match(linha)

print(m)
print(a)
print(b)
print(c)
print(d)




# print(m.span())
# print(m.end())







