import re
#1
txt = 'the cat is on the roof'
x=re.search("cat",txt)
if x :
    print(f"yes the cat appears and the index position is {x.start()}")
else:
    print("no the cat didn't appeared")


# 2
txt = "There are 12 cats, 4 dogs, and 7 birds."
x=re.findall(r'\d+',txt)
print(x)


# phone number validation 
txt ="123 456-9890"
x = re.match(r"\d{3} \d{3}-\d{4}",txt)
print(x is not None)

# Find Words Starting with a Vowel
txt ='An elephant is in the open area'
x = re.findall(r"\b[aeiouAEIOU]\w*",txt)
print(x)


#match dates 
txt = "Today's date is 30/12/2024, and tomorrow is 31/12/2024."
x = re.findall(r"\b\d{2}/\d{2}/\d{4}",txt)
print(x)


#replace multiple 
txt = "This    string   has   too  many   spaces."
x = re.sub(r"\s+"," ",txt)
print(x)

#Extract Hashtags from a Tweet
txt = "Loving the weather! #sunny #beautiful #nature"
x = re.findall(r"#\w+",txt)
print(x)

#email match 
txt = ["test@example.com", "invalid-email@", "user@domain.org"]
x= [email for email in txt if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email)]
print(x)