# class Car:
#     def __init__(self,color,brand):
#         # print(self)
#         self.color=color
#         self.brand=brand

#     def get_brand(self):
#         return self.brand
    
#     def get_color(self):
#         return self.color
    
#     def __str__(self):
#         return f"Car brand {self.get_brand()} created"

# car1=Car("black","BMW")
# print(car1.color)
# print(car1)
# print(car1.get_brand())
# print(car1.get_color()) 




class Student:
    def __init__(self,name,marks):
         self.name=name
         self.marks=marks

    def avg_marks(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f'hi {self.name} your avg score is {sum//3}')
    
    @staticmethod
    def hello():
        print("its a static method or function")



eran=Student('eran',[98,90,90])
eran.avg_marks()
eran.name='goud'
eran.avg_marks()
Student.hello()


def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator  # Apply the decorator to a function
def say_hello():
    print("Hello!")

say_hello()
