# abstract class - a class which contains one or more abstract methods.
# abstarct methods = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go (self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go (self):
        print("Your drive the car")

    def stop(self):
        print("This car is stopped")
        

class Motorcycle(Vehicle):

    def go (self):
        print("You ride on motorcycle")

    def stop(self):
        print("This motrocycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#car.stop()
motorcycle.stop()

