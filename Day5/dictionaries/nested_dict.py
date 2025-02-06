#Nested Dictionary Operations

student = {
    'name': 'John',
    'marks': {'math': 90, 'science': 85, 'english': 88}
}

print(student['name'],student['marks']['science'])
student['marks']['history']=50
print(student['marks'])