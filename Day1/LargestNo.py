# def Largest_no(num):
#     largest_no=0
#     while num>0:
#         digit= num %10
#         if digit>largest_no:
#             largest_no=digit
#         num//=10
#     print(largest_no)
        

# Largest_no(112345678923)

num=int(input("enter the digit to find largest number:"))
digits=[int(digit) for digit in str(num)] # list comprehension method
largest_no=max(digits)
print(f"the largest digit is {largest_no}")