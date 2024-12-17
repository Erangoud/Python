# num=int(input("enter the number"))
# total = 0
# while num>0:
#     total+=num%10
#     num//=10
# print(f"the sum of digits are {total}")


num = input("enter the number:")
total=sum(int(digit) for digit in num)
print(f"sum of digits: {total}")