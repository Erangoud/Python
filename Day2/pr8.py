"""
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
"""

n=6
for i in range(n+1):
    if i==6 or i==3:
        continue
    else:
        print(i,end=" ")