import string
from random import *

filename = 'banned-passwords.txt'
characters = string.ascii_letters + string.punctuation  + string.digits

for p in passwords:
    password =  p.join(choice(characters) for x in range(randint(1, 6)))
    with open(filename, 'a') as file_object:
        file_object.write(password + "\n")

for p in passwords:
    password2 = "".join(choice(characters) + p for x in range(randint(1, 6)))
    with open(filename, 'a') as file_object:
        file_object.write(password2 + "\n")


for l in passwords:
    password3 = l + choice(string.punctuation) + choice(string.digits) + choice(string.digits) + choice(string.digits)
    with open(filename, 'a') as file_object:
        file_object.write(password3 + "\n")




