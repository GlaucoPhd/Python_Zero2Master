Matrix = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill = '$'
empty = ' '

for row in Matrix:
	for pixel in row:
		if pixel:
			print(fill, end='')
		else:
			print(empty, end='')
	print('')

for row in Matrix:
	for pixel in row:
		if pixel:
			print(fill, end='')
		else:
			print(empty, end='')
	print('')

	for row in Matrix:
	for pixel in row:
		if pixel:
			print(fill, end='')
		else:
			print(empty, end='')
	print('')

	for row in Matrix:
	for pixel in row:
		if pixel:
			print(fill, end='')
		else:
			print(empty, end='')
	print('')



# If case to use more than once
# Should be better idea
# We cant assigned another value
# Whitou change all the code
# for row in Matrix:



# 	# if (pixel REMOVE  == 1):
# 	# also REMOVE ()