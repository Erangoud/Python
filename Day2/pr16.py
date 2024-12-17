# n=[]
# for i in range(100,400+1):
#     digits=str(i)
#     if (int(digits[0])%2==0) and (int(digits[1])%2==0) and (int(digits[2])%2==0) :
#         n.append(i)
# print(",".join(map(str,n)))
# print(n)


# for i in range(100,401):
#     temp=i
#     while temp>0:
#         digit=temp%10
#         if not digit%2==0:
#             break
#         temp//=10
#     if temp==0:
#         print(i,end=" ")


def verify_even_digit(n):
    flags=[]
    for digit in str(n):
        if int(digit)%2!=0:
            flags.append(False)
        flags.append(True)     
    return all(flags)
    
def print_even_odd(a,b):
    for i in range(a,b+1):
        if verify_even_digit(i):
            print(i,end=" ")

print_even_odd(200,700)