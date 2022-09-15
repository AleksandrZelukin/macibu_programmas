# abstract class - a class which contains one or more abstract methods.
# abstarct methods = a method that has a declaration but does not have an implementation.



class Vehicle:
    def go (self):
        pass
class Car(Vehicle):

    def go (self):
        print("Your drive the car")

class Motorcycle(Vehicle):

    def go (self):
        print("You ride on motorcycle")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

