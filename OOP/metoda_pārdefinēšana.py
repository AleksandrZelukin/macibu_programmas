class One:
    def __init__(self, name):
        self.name = name
    def talk(self):
        return f'Mani sauc {self.name}'
    def say(self):
        return f'Sveiki {self.name}'
           
class Two(One): # metoda dekoracija                
    def say(self):
        x = One.say(self)
        return f'{x} !!!'
           
class Three(One): # metoda pārdefinēšana                    
    def say(self, word):
        return f'{word} {self.name}...'
        
        
one = One('Andris')
two = Two('Jānis')
three = Three('Aija')

#rezultata izvade
print(f'class {One.__name__}:')
print(one.talk())
print(one.say())
# class One:

print(f'class {Two.__name__}:')
print(two.talk())
print(two.say())
print('Two is subclass One:', issubclass(Two, One))
# class Two:

print(f'class {Three.__name__}:')
print(three.talk())
print(three.say('Čau'))
print('Three is subclass One:', issubclass(Three, One))

print('Three is subclass Two:', issubclass(Three, Two))
# Three is subclass Two: False