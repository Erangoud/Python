#Find the Largest of Three Numbers

a=int(input("enter the first digit A : "))
b=int(input("enter the first digit B : "))
c=int(input("enter the first digit C : "))

if a > b and a > c:
    print(f"the largest digit is {a}")
elif b > c :
    print(f"the largest digit is {b}")
else:
    print(f"the largest digit is {c}")