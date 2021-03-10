# # Data Types
# # None
# # bool
# # int
# # float
# #
# # # Complex
# # str
# # list
# # tuple
# # set
# # dict
# #
# # # custom types
# # classes
# #
# # # Specialized Data Type
# # __init__

from collections import Counter, defaultdict, OrderedDict

li = [1, 3, 2, 4, 5, 6, 7, 7]
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
sentence = 'Bla bla bla thimk about pytho'
d = OrderedDict()
d['a'] = 1
d['b'] = 2

print(Counter(li))
print(Counter(sentence))
print(dictionary['a'])
print(dictionary['c'])





