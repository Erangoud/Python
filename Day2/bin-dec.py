# binary=input("enter the decimal number:")
# decimal= int(binary,2)
# print(decimal)
"""
What is a base?
Numbers can be represented in different bases:
Base 10 (decimal): Regular numbers we use daily (0, 1, 2, ..., 9).
Base 2 (binary): Numbers represented using only 0 and 1.
Base 16 (hexadecimal): Numbers represented using 0–9 and A–F.

"""


bin=input("enter the bin:")
dec=0
for bit in bin:
    dec=dec*2+int(bit)
    # print(dec)# you can use this for check 
print(dec)