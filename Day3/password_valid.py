'''Write a  Python program to check the validity of passwords input by users.

Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.'''


# import re 

# password=input("enter the password : ")

# x=True

# while x:

#     if (len(password) <6 or len(password) > 16) :
#         break
#     elif not re.search('[a-z]',password):
#         break
#     elif not re.search('[A-Z]',password):
#         break
#     elif not re.search('[0-9]',password):
#         break
#     elif not re.search('[@#$]',password):
#         break
#     else:
#         print('its a valid password')
#         x=False

# if x:
#     print("not a valid password ")


passw=input("enter the password : ")

x= True

while x :
    if len(passw)<6 or len(passw)>12:
        break
    lower=sum(1 for char in passw if char.islower())>=2
    upper=any(char.isupper()for char in passw)
    leng=any(char.isdigit for char in passw)
    exp=any(char in '@#$' for char in passw)

    if not lower:
        break
    if not upper:
        break
    if not leng:
        break
    if not exp :
        break

    print('the password is valid ')
    x=False

if x :
    print ('not a valid password')