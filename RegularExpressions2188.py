import re

# pattern = re.compile('Meu')
# linha = 'Meu amigo, vc sabe como Meu dia foi hoje.'
#
# a = pattern.search(linha)
# b = pattern.findall(linha)
# c = pattern.fullmatch(linha)
# d = pattern.match(linha)
# e = re.findall("[a-m]", linha)
# f = re.match()
#
#
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

pattern_a = re.compile(r"([a-zA-Z]).([a])")
string = "Search this inside of this text please! Andrei"
# Re group we can get part of the group output
f = pattern_a.search(string)
print(f.group(1))
print(f.group(2))





