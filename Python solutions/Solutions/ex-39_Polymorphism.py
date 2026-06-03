class Employee:
    def work(self):
        print("Employee is working")
class developer(Employee):
    def work(self):
        print("Developer writing code")
class tester(Employee):
    def work(self):
        print("Tester testing application")
employees=[developer(),tester()]
for emp in employees:
    emp.work()                  