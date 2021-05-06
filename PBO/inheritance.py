class Person(object):

    # constructor
    def __init__(self, name):
        self.name = name
    
    # to get name
    def getName(self):
        return self.name
    
    # to check if this person is an employee
    def isEmployee(self):
        return False
    
# Inherited or subclass (note person in bracket)
class Employee(Person):

    # here we return true
    def isEmployee(self):
        return True
    
# Driver code
emp = Person("Sam") # an object of person
print(emp.getName(), emp.isEmployee())

emp = Employee("Chris") # an object of employee
print(emp.getName(), emp.isEmployee())