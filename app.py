import string
from random import choices


length = int(input("Enter password length: "))

pass_initial = ''

Uppercase_letters = input("Include uppercase letters? (y/n): ").lower()

if Uppercase_letters == 'y':
    pass_initial += ''.join(choices(string.ascii_uppercase, k=length))


numbers = input("Include numbers? (y/n): ").lower()

if numbers == 'y':
    pass_initial += ''.join(choices(string.digits, k=length))

special_characters = input("Include special characters? (y/n): ").lower()

if special_characters == 'y':
    pass_initial += ''.join(choices(string.punctuation, k=length))


password = ''.join(choices(pass_initial, k=length))
print(f"Generated password: {password}")
