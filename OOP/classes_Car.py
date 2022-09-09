# https://youtu.be/K86vSI5gfGA
class Car:
    count_of_wheels = 4

    def __init__(self, color, speed, mark, place = None):
        self.color = color
        self.speed = speed
        self.mark = mark
        self.place = place
        

    def drive (self,place):
        print(f'Auto {self.mark} {self.color} krasa brauc ar atrumu {self.speed}km/h uz {self.place}')

car1 = Car('Sarkana', 90, 'Toyota')

print(car1.mark, car1.speed, car1.color)

car1.drive('Daugavpils')

print('auto brauc uz',car1.drive)

print('Ka ari manai masinai ir', car1.count_of_wheels, 'ritenus.\n')
