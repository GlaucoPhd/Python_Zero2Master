# == checking equality or rquality of value
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# is check equality,value and Location  
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([1,2,3] is [1,2,3])

print(True is True)
print('1' is '1')
print([] is []) #Is in the same location?
print(10 is 10)
print([1,2,3] is [1,2,3]) #Is same list but create in a new location