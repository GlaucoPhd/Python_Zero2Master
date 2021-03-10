user = {
'basket': [1,2,3],
'greet': 'hello',
'age': 20
}

print('age' in user.keys()) #1
print('hello' in user.values()) #2
print(user.items()) #3
user2 = user.copy()
print(user) #4
#Copy create and generate another user
print(user.clear()) #5
print(user2) #6
print(user.update({'age':55}))
#POP remove the value ywe user
#Print again just disapear the value

