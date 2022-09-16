class Vehicle:
    def go (self):
        pass

class Car(Vehicle):
    def go (self):
        print("Your drive the car")

class Motorcycle(Vehicle):
    def go (self):
        print("You ride the motorcycle")

        
vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
car.go()
motorcycle.go()
