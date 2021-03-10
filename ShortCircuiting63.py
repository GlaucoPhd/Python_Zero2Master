#Short Circuiting
is_friend =True
is_user = True

if is_friend and is_user:
	print('best friends forever')

if is_friend or is_user:
	print('best friends forever')

friend = False
user = True
if False and user:
	print('Best Friends')