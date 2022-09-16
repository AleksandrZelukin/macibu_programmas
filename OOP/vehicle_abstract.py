from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go (self):
        pass    
    @abstractmethod
    def stop (self):
        pass
    
class Car(Vehicle):
    def go (self):
        print("Your drive the car")
    def stop (self):
        print("This car is stopped")
        

class Motorcycle(Vehicle):
    def go (self):
        print("You ride on motorcycle")
    def stop (self):
        print("This motorcycle is stopped")

        
car = Car()
motorcycle = Motorcycle()
car.stop()
motorcycle.stop()
