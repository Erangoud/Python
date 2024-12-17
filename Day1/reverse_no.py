num=int(input("enter the number : "))#1234
reverse__num=0
while num>0:
    digit=num%10
    reverse__num=reverse__num*10+digit  # 0*10+4=4   4*10+3=43  43*10+2=432  432*10+1=4321
    num//=10
print(reverse__num)