
class Public:
    global age
    age = 36
    def __init__(self,name):
        self.name = name 

         # Public attribute

    def display_name(self):
        print(self.name,age)  # Public method

obj1 = Public('eran')
eran=Public('win')

print(obj1)
obj1.display_name()  # Accessible
print(obj1.name)  # Accessible