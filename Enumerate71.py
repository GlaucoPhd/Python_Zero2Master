# for i,char in enumerate('Hello'):
# 	print(i, char)
# print('\n')

# for i,char in enumerate([1,2,3,4]):
# 	print(i, char)
# print('\n')

# for i,char in enumerate((1,2,3,4)):
# 	print(i, char)

for i,char in enumerate(list(range(70))):
	if char == 50:
		print(f'Index of 50 is: {i}')

