user_name = input('Name: ')
password = input('Password: ')
password_lengh = len(password)
hidden_password = '*' * password_lengh
print(f'User name {user_name}, your password {hidden_password} is {password_lengh} characteres long.')



