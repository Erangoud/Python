num=int(input("enter a number: "))
power=len(str(num))
total=0
temp=num
while temp>0:
    total=total+(temp%10)**power
    temp//=10
print("arm strong" if num==total else "not a arm strong")


# num = int(input("Enter a number: "))
# power = len(str(num))
# total = sum([int(digit) ** power for digit in str(num)])
# print("Armstrong Number" if total == num else "Not an Armstrong Number")


#153,1634

