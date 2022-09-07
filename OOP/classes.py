#Piemers 1
class A:
    pass

#Piemers 2
class B: 
    pass
    
a = B()
b = B()
c = B()

a.arg = 10 # у экземпляра a появился атрибут arg
b.arg = 20

print(a.arg)
print(b.arg)

#piemers 3
class C: 
    def g(self): # self - обязательный аргумент, содержащий в себе экземпляр
                 # класса, передающийся при вызове метода,
                 # поэтому этот аргумент должен присутствовать
                 # во всех методах класса.
        return "Hello!"
    
a = C()

print(a.g())


#Piemers 4
class D:
    def __init__(self, name):
        self.name = name
q = D('Anna')
print(q.name)
    