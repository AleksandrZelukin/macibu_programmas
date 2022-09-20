# https://youtu.be/K86vSI5gfGA
class Car:
    count_of_wheels = 4
    #print(f'Ka ari manai masinai ir {count_of_wheels} ritenus.\n')
    
    def __init__(self, color, speed, mark):
        self.color = color
        self.speed = speed
        self.mark = mark
        
    def drive (self,place):
        self.place = place
        print(f'Auto {self.mark} {self.color} krasa brauc ar atrumu {self.speed}km/h uz {self.place}')

car1 = Car('sarkana', 90, 'Toyota')

print(car1.mark, car1.speed, car1.color)

car1.drive('Daugavpils')

print('Ka ari manai masinai ir', car1.count_of_wheels, 'ritenus.\n')

