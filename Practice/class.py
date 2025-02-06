def prime_numbers(n):
    for num in range(2,n+1):
        for div in range(2,int(num**0.5)+1):
            if num%div==0:
                break
        else:
            print(num,end=" ")

prime_numbers(100)