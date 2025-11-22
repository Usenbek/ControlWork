#1

class Person:
    def __init__(self, age = None):
        self._age = age
    def set_age(self, age):
        self._age = age
        if self._age < 0:
            print("Предупреждение: такого возраста не может быть")
    def get_age(self):
         print(self._age)
# p = Person()
# p.set_age(20)
# p.get_age()
# p.set_age(-5)

#2

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "i am an animal"
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
dog = Dog("Buddy")
cat = Cat("Kitty")
#
# print(dog.name, dog.speak())
# print(cat.name, cat.speak())
class Vehicle():
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is moving"
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()
car = Car()
bike = Bicycle()
# print(move(bike))

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
rectangle = Rectangle(10, 20)
print(rectangle.area())
circle = Circle(7)
print(circle.area())


