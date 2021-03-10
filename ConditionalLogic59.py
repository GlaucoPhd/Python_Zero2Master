#Conditional Operation : generate identation
#If ist true run everthing down bellow
is_old = True  #Runs the If, chamge to False just skip
is_licenced = True

if is_old:
	print('You are old enough to drive!')
else:
	print('You are not of age')
print('Checkcheck')

###############################
is_older = True   
is_licences = True

if is_older:
	print('You are old enough to drive!')
elif is_licences:
	print('You can drive now')
else:
	print('You are not of age')
print('Checkcheck')

###############################
is_olderest = True   
is_licenced = True

#Only Both are true you can drive
if is_olderest and is_licenced:
	print('You are old enough to drive, and have a License')
else:
	print('You are not of age')
print('Checkcheck')