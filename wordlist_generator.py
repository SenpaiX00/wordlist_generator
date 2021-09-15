import string
from random import *

passwords = ["WORDS","GO","HERE"] #words can be scraped from sites using CEWL tool
characters = string.ascii_letters + string.punctuation  + string.digits

for p in passwords:
    password =  p.join(choice(characters) for x in range(randint(1, 6)))
    print password

for p in passwords:
    password2 = "".join(choice(characters) + p for x in range(randint(1, 6)))
    print password2


for l in passwords:
    password3 = l + choice(string.punctuation) + choice(string.digits) + choice(string.digits) + choice(string.digits)
    #password3 = l.join(choice(string.punctuation)) + choice(string.digits)
    print password3




