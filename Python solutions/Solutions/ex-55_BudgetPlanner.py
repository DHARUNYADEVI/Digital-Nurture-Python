class BudgetPlanner:
    def __init__(self, income):
        self.income = income
        self.expenses = []
    def add_expense(self, amount):
        self.expenses.append(amount)
    def total_expenses(self):
        return sum(self.expenses)
    def savings(self):
        return self.income - self.total_expenses()
planner = BudgetPlanner(50000)
planner.add_expense(10000)
planner.add_expense(5000)
planner.add_expense(8000)
print("Income:", planner.income)
print(
    "Total Expenses:",
    planner.total_expenses()
)
print(
    "Savings:",
    planner.savings()
)