import csv
def expense_tracker():
    category_totals = {}
    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["amount"])
            category = row["category"]
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += amount
    print("Expense Summary")
    for category, total in category_totals.items():
        print(category, ":", total)
expense_tracker()