#Example Code

import random
from unittest import case
import pyperclip

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

length = input("Hey, specify the length of your password? (default 128)\n")
length = 128  if length == '' else int(length)

while True:

    option = input("choose the option you want you password to have\n0-lower case caracter\n1-upper case caracter\n2-number\n3-special character\n your input should be in form '1,2,0'\n");
    ca=True
    opt= option.split(',');
    j=0
    for i in opt:
        opt[j]=int(i)
        if opt[j]>3 or opt[j]<0:
            ca=False
        j+=1
    if ca:
        break

#randomly select ascii character classes and individual characters


while count < length:
    rand = random.choice(opt)
    print(rand)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,122))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,90)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,58)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,48)
            password.append(b)
        elif r == 1:
            b = random.randint (91,96)
            password.append(b)
        elif r == 2:
            
            b = random.randint (123,126)
            password.append(b)
    count += 1

#convert ascii code to characters
word = "".join([chr(c) for c in password])

#copy pass to clipboard
pyperclip.copy(word)

#print the result
print ("Random password of length %s is: \n" % length)

print('******')
print(word)
print('******')

print ("\nIt contains",lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol characters")
input('Password copied to clipboard, push a button to exit...')
