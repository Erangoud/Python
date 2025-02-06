class automobile:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    # def __str__(self):
    #     return 
    def display_price(self):
        print(f"The {self.name} price is {self.price}")
    
suziki=automobile("switf",1000000)
print(suziki)

 


# class my_class:
#     class_attribute="this is attribute"

#     def greet(self):
#         print('hello,world')

# obj=my_class()
# print(obj.class_attribute)
# print(obj.greet())


