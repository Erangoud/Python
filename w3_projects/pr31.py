"""
Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73
"""

human_year=float(input("enter the age of a human:"))
if human_year<=2:
    dog_year=human_year*10.5
else:
    dog_year=2*10.5 + (human_year - 2)*4
# dog_y=int(dog_year)
print(f"the dog age according to dog's year {int(dog_year)}")