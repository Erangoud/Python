# print("hello,world!")
n=2
while n<=50:
    count =0
    for i in range(1,(n//2)+1):
        if n%i==0:
            count+=1
    if count>1 :
        print(f"{n} not a prime")
    else:
        print (f"{n} prime")
    n+=1