class Employee:  
    """Bazes klase darbinieki"""  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Kopa darbinieki: %d' % Employee.emp_count)
        
    def display_employee(self):  
        print('Darbinieka vards, alga: {}. Alga: {}'.format(self.name, self.salary))  
  
  
# pirmais objekts klase Employee  
emp1 = Employee("Andris", 550)  
# otrais objekts klase Employee  
emp2 = Employee("Anna", 600)  
emp1.display_employee()  
emp2.display_employee()  
print("Kopa darbinieki: %d" % Employee.emp_count)