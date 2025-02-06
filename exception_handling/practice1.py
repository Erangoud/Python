# a=input("enter the number")
# print(f" multiplication table of :{a}")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e :
#     print(e)

# try:
#     num=int(input("enter the number"))
#     a=[6,4]
#     print(a[num])
# except ValueError:
#     print("the entered value is not an integer ")
# except IndexError:
#     print("index error")

def func1():
    try:  
        i=[1,2,3,4,4]
        l=int(input("enter the number"))
        print(i[l])
        return 0
    except IndexError:
        print("its an index error")
    finally:
        print("always executed")

x=func1()
print(x)


# def func2():
#     try:
#         l=[1,2,3,4,5]
#         i=int(input("enter the index between"))
#         print(l[i])
#     except IndexError:
#         print("out of index range")
#     except ValueError:
#         print("only number")
#     finally:
#         print("completed")
    
# x=func2()

# x =-1
# if x<0:
#     raise Exception("sorry number should be greater then 0")