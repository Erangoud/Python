# num=int(input("enter the decimal number:"))
# print("binary:",bin(num)[2:])

dec=int(input("enter the decimal no.:"))
binary= ""
while dec>0:
    binary=str(dec%2)+binary
    dec//=2
print(binary)