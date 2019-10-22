#Opertor Overloading
# __init__ is dunder method as it is a constructor


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    def __add__(self,other):        #Operator overloading
        return self.salary+ other.salary
    def __truediv__(self, other):
        return self.salary/ other.salary
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
emp1= Employee("Amit", 350, "Programmer")
emp2= Employee("Manu", 450, "Programmer")
print(emp1+emp2)
print(emp1/emp2)
print(emp1)
print(str(emp1))