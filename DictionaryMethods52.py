#Dictionary are immutiable
#Overwrite a key
user = {
'basket' : [1,2,3],
'greet' : 'Hi', 
'age': 20

}

#Get found key print the original value
print(user['basket'])
print(user.get('age', 55))
print(user.get('password'))

usuario = dict(name = 'Glauco')
print(usuario)

