#Break works for Loops and While and takes it out of the loop 
#continue get the string back to the loop
#Example continue Loop Shows how it work in a middle of a loop
#Pass good way when you dont have the idea to code the block

print('\n Example 1 - For Break Loop')
my_list = [1,2,3]
for item in my_list:
	print(item)
	break

print('\n Example 2 - While Break Loop')
i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
	break

print('\n Example 3 - For Continue Loop')
my_list = [1,2,3]
for item in my_list:
	print(item)
	continue

print('\n Example 4 - While Continue Loop')
i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
	continue

print('\n Example 5 - For Pass Loop ')
my_list = [1,2,3]
for item in my_list:
	pass
	print(item)

print('\n Example 6 - While Pass Loop')	
i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1
	pass

print('\nExample of a continue loop that  never will be printed.')

my_list = [1,2,3]
for item in my_list:
	continue
	print(item)



