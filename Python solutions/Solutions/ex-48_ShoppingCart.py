class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, name, price):
        self.items.append({
            "name": name,
            "price": price
        })
    def total(self):
        return sum(item["price"] for item in self.items)
    def display(self):
        print("Cart Items")
        for item in self.items:
            print(item["name"], "-", item["price"])
        print("Total:", self.total())
cart = ShoppingCart()
cart.add_item("Laptop", 50000)
cart.add_item("Mouse", 500)
cart.display()