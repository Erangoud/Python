# num = input("Enter a number: ")
# if num == num[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


num=int(input("enter a number :"))
original= num
reverse= 0
while num>0:
    reverse=reverse*10 +num%10
    # print(num,reverse) 
    num//=10

print("its a palindrom" if original==reverse else "not a palindrom")