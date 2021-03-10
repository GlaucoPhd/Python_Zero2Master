#Dictionary (Hash table)
#Data Structure way to organize the Data
#unordered values
#Print big Dictionary the order will not be followed
Dictionary = {
'a' : 1,
'b' : 2
}
print(Dictionary['b'])
print(Dictionary)

Dictionary = {
'a' : [1,2,4],
'b' : 'qwer',
'c' : True
}

print(Dictionary)
print(Dictionary['c'])

my_list = [
{
'j' : [9,8,6],
'k' : 'yuoi',
'l' : False
},
{
'j' : [5,7,0],
'k' : 'yuoi',
'l' : False
}
]
print(my_list[0]['j'])
print(my_list[0]['l'])
print(my_list[1]['k'][1])
#Dictionary Print 0,1,2 is the location
print(my_list[1]['j'][2])