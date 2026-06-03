class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def from_string(cls,data):
        name,salary=data.split(",")
        return cls(name,int(salary))
    def display(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
employee=employee.from_string("Shubh,75000")
employee.display()           