"""Encapsulation"""

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def deposite(self,amount):
#         if amount <= 0 :
#             print("invalid amount")
#         else :
#             self.__balance +=amount
        
#     def get_balance(self):
#         return print(self.__balance)
    
#     def Withdraw(self,amount):
#         if amount > self.__balance:
#             print("insufficieint amount")
#         else :
#             self.__balance -= amount
#         print("withdrawed successfully")



# emp1=BankAccount(123,500)
# emp1.deposite(200)
# emp1.get_balance()
# emp1.Withdraw(200)
# emp1.get_balance()


"""Inheritance"""

# class User:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
    
#     def login(self):
#         return f"{self.name} is logged in good "

# class Seller(User):
#     def __init__(self, name, email,shop_name):
#         super().__init__(name, email)
#         self.shopname=shop_name

#     def add_cart(self,product):
#         return f"{product} added to the cart from shop "

# person1 = Seller("eran","egoud","D-mart")
# print(person1.add_cart("bujji"))
# print(person1.login())



""" abstraction """

# from abc import ABC,abstractmethod

# class Animal(ABC) :
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         return "woof"
    

# p1=Dog("husky")
# print(p1.sound())


"""@Class Method """

class Mehtod:
    company="Bridgelabz"
    def __init__(self,name):
        self.name=name
    
    @classmethod
    def modify_name(cls,name2):
        cls.company=name2

    @staticmethod
    def stat():
        print("welcome to staticmethod ")

p1=Mehtod("eran")
print(p1.name)
print(p1.company)
Mehtod.modify_name("wipro")
print(p1.company)
p1.stat()

# import re 
# txt ="the spain in rain"
# x = re.sub("\s","6",txt)
# print(x)