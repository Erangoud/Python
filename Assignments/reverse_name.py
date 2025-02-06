#1. Write a Python program which accepts the user's first and last name and print them in
#reverse order with a space between them.

first_name=input("enter the first name : ")
last_name=input("enter the last name : ")

print(last_name[::-1],first_name[::-1])


#----------------------------------

full_name = [first_name, last_name]
print(" ".join(name[::-1] for name in full_name))