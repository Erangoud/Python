word=input("enter the word : ")
vowels='aeiouAEIOU'
count=0

for char in (word):
    if char in vowels:
        count+=1

print(f"the total vowels present in the sentences are : {count}")