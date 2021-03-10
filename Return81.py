# Functions always return something, if dont return any value the output will be none

def sum(num1, num2):
	def another_func(num1, num2):
		return num1 + num2
	return another_func

total = sum(10, 20)
print(total(10, 20))

sum(10, 20)


def mais(n1, n2):
	def mais_1(n1, n2):
		return n1 + n2
	return mais_1
total = mais(1, 32)
print(total(32, 32))


print(mais(0, 2))
