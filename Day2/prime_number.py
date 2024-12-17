# n=2 
# while n<=50:
#     count=0
#     for i in range(1,n//2+1):
#         if n%i==0:
#             count+=1
#     if count>1:
#             print (f"{n} not a prime ")
#     else:
#             print (f"{n} prime ")
#     n+=1

def prime_num(n):
    for num in range(2,n+1):
        for div in range(2,int(num**0.5)+1):
            if num%div==0:
                break
        else:
            print(num,end=" ")

prime_num(100)
