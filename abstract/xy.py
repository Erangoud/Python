from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def sound(self):
        pass  # Abstract method

    def sleep(self):  # Concrete method
        print("This animal is sleeping.")


class Dog(Animal):  
    def sound(self):  
        print("Woof Woof!")

class Cat(Animal):
    def sound(self): 
        print("Meow Meow!")


dog = Dog()
dog.sound()  
dog.sleep()  

cat = Cat()
cat.sound() 
cat.sleep() 