import re

with open(r"C:\Users\egoud\OneDrive\Documents\Desktop\Economic Survey 2025 LIVE Finance M.txt","r") as file :
    pattern =r"survey[a-z]+*the$"
    r = file.read()
    print(re.search(pattern,r))
    # print(file.read())