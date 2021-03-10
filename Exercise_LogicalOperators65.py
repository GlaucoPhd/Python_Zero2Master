#PC is really smart
#Focus write as emglish simple and nice
is_magician = False
is_expert = False

if is_magician or is_expert:
	print('Master')
if is_expert:
	print('Medium')
if not is_magician:
	print('Beginner')

# Using If and elif
if is_expert and is_magician:
	print('Master')
elif is_magician and not is_expert:
	print('Medium')
elif not is_magician:
	print('Beginner')