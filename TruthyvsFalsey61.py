check_user = input('Insert your user: ')
user = ['a','Glauco','b','c','d','e','d']
password = '234'

if check_user in user:
	print('You already have an account!\n')
else:
	print('Please create your account')
if check_user != user:
	 new_user = input('Insert a user name: ')
	 new_password = input('Inset a password: ')
	 email = input('Insert your email to confirm your account: ')
	 print('We sent an email to you, please just confirm and login.')
	
# password = '234'
# user = 'Glauco'
# a = input('Reset Password Yes or No:')
# if password and user:
# 	print('You already have an account!\n')
# 	#	a = ('Yes')
# 	#	print('Ok')
# # else:
# 	#print('No problem, Thanks.')

# 	a = input('Reset Password Yes or No:')