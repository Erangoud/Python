# a=int(input("enter the number :"))
# x=0
# y=1

# while y<a:
#     print(y,end=" ")
#     x,y=y,x+y
  


def fib(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

def printfib(n):
    i = 0
    while True:
        fib_num = fib(i)
        if fib_num > n:  # Stop when the Fibonacci number exceeds 50
            break
        print(fib_num, end=' ')
        i += 1
printfib(50)