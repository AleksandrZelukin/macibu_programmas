class a:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Alex = a('Alex', 20)
Amanda = a('Amanda', 30)
David = a('David', 15)
b = [Alex, Amanda, David]

b.sort(key=lambda x: x.age)
print([item.name for item in b])
# вывод: ['David', 'Alex', 'Amanda']
