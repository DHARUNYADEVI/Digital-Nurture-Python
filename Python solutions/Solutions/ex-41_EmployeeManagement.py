import json
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"
employees = {}
def add_employee():
    emp = Employee(101, "Dharunya", 50000)
    employees[emp.emp_id] = {
        "name": emp.name,
        "salary": emp.salary
    }
    print("Employee Added Successfully")
def save_data():
    with open("emps.json", "w") as file:
        json.dump(employees, file, indent=4)
    print("Data Saved Successfully")
def load_data():
    try:
        with open("emps.json", "r") as file:
            data = json.load(file)
            print("\nEmployee Records")
            for emp_id, details in data.items():
                print(
                    f"ID: {emp_id}, "
                    f"Name: {details['name']}, "
                    f"Salary: {details['salary']}"
                )
    except FileNotFoundError:
        print("No File Found")
add_employee()
save_data()
load_data()