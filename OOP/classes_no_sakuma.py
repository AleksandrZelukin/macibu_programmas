class Cat:
    cute = "Ķaķis ir miļš"
    def __init__(self, name, age, poroda):
        self.name = name
        self.age = age
        self.poroda = poroda

milo = Cat("Milo",2, None)
simba = Cat("Simba", 3, None)

print(milo.name, milo.age)

