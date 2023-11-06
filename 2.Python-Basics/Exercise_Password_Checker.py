username = input("Please enter your username:")
password = input('please enter your password:')
# password_length_as_str = str(len(password))
password_length = len(password)
marked_password = "*" * password_length
print(f'{username}, your password, {password}, is {len(password)} letters long.')
print(f"Hey {username}, your password {marked_password} is {password_length} letters long.")
