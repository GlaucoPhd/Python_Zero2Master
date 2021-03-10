#For simple loops or interanting with objects. Best option
for item in [1,2,3]:
	print(item)
print('\n')

#While are very flexible, if dont have any ideia how many time ou how long it take to loop use while.The point is you need to remeber about a create a variable, to avoid infinite loop 
i = 0
while i < len([1,2,3]):
	print(i)
	i += 1
print('\n')

my_list = [1,2,3]
i = 0
while i < len(my_list):
	print(i)
	i += 1
print('\n')

while True:
	print(my_list[0])
	break

while True:
	input('Name: ')
	break
print('\n')

while True:
	response = input('Say: ')
	if (response == 'bye'):
		break