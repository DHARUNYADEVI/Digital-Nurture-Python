class Employee:
    def __init__(self):
        self.salary=0
    def set_salary(self,amount):
        self.salary=amount
        return self
    def add_raise(self,amount):
        self.salary+=amount
        return self
    def display(self):
        print("Final Salary: ",self.salary)
        return self
employee=Employee()
employee.set_salary(50000)\
        .add_raise(5000)\
        .display()