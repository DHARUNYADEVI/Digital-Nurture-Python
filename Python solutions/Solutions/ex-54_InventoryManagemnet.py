class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self, name, qty):
        self.products[name] = qty
    def update_stock(self, name, qty):
        if name in self.products:
            self.products[name] += qty
    def display(self):
        print("Inventory")
        for product, qty in self.products.items():
            print(product, ":", qty)
inventory = Inventory()
inventory.add_product("Laptop", 10)
inventory.update_stock("Laptop", 5)
inventory.display()