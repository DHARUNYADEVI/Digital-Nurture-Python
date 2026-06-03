import csv
def process_csv():
    employees = []
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["salary"] = int(row["salary"])
            employees.append(row)
    high_salary = [
        emp for emp in employees
        if emp["salary"] > 50000
    ]
    average_salary = sum(
        emp["salary"]
        for emp in employees
    ) / len(employees)
    print("High Salary Employees:")
    for emp in high_salary:
        print(emp["name"])
    print("Average Salary:", average_salary)
process_csv()