class Employee():
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Employee name: ",self.name)
emp1=Employee("DharunyaDevi")
emp2=Employee("Ravi")
emp3=Employee("Priya")
emp1.display()
emp2.display()
emp3.display()            
        