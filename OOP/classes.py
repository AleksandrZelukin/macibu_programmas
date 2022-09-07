class A:
    pass


class B: 
    pass
    
a = B()
b = B()
c = B()

a.arg = 10 # у экземпляра a появился атрибут arg
b.arg = 20

print(a.arg)
print(b.arg)


class C: 
    def g(self): # self - обязательный аргумент, содержащий в себе экземпляр
                 # класса, передающийся при вызове метода,
                 # поэтому этот аргумент должен присутствовать
                 # во всех методах класса.
        return "Hello!"
    
a = C()

print(a.g())
