def calculate_net_salary(salary,tax_rate):
    if salary < 0 or tax_rate < 0:
        return("Invalid input. Salary and tax rate must be non-negative.")
    net_salary=salary-(salary*tax_rate)
    return net_salary
salary=75000.5
tax_rate=0.18
result=calculate_net_salary(salary,tax_rate)
print(f"Net Salary: {result:.2f}")
    