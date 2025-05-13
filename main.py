class Product:
    def __init__(self, product_id, name, price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}), Price: ${self.price}, Stock: {self.quantity_in_stock}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Error: Product ID {product.product_id} already exists.")
        else:
            self.products[product.product_id] = product
            print(f"Product '{product.name}' added successfully.")

    def list_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products.values():
                print(product)


def cli_menu():
    inventory = Inventory()
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. List Products")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            product_id = input("Enter product ID: ").strip()
            name = input("Enter product name: ").strip()
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity in stock: "))
            product = Product(product_id, name, price, quantity)
            inventory.add_product(product)

        elif choice == "2":
            print("Products in inventory:")
            inventory.list_products()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    cli_menu()
