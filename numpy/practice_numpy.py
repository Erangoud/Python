# # import numpy as np
# # arr=np.array([1,2,3,4,5])
# # print(arr)


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

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    
    def login(self):
        return f"{self.name} is logged in good "

class Seller(User):
    def __init__(self, name, email,shop_name):
        super().__init__(name, email)
        self.shopname=shop_name

    def add_cart(self,product):
        return f"{product} added to the cart from shop "

person1 = Seller("eran","egoud","D-mart")
print(person1.add_cart("bujji"))
print(person1.login())




