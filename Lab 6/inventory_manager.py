import json
import os
# Create Product class
class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

# Create Inventory class
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.product_id) is not None:
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.product_id == product_id:
                return product

        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 48)

        if not self.__products:
            print("No products in inventory.")
        else:
            for product in self.__products:
                product.display_information()

        print("-" * 48)

    def get_products(self):
        return self.__products.copy()

# Save Product objects to JSON
def save_inventory(inventory):
    print("Saving inventory...")

    data = []

    for product in inventory.get_products():
        data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


# Load JSON data as Product objects
def load_inventory(inventory):
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    else:
        print("inventory.json not found.")

# Display menu for user 
def main():
    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            print("\nAdd New Product")

            product_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()

            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
            except ValueError:
                print("Invalid price or stock.")
                continue

            if not product_id or not name or price < 0 or stock < 0:
                print("Invalid product details.")
                continue

            new_product = Product(
                product_id, name, price, stock
            )

            if inventory.add_product(new_product):
                print("Product added successfully!")
            else:
                print("Product ID already exists.")

        elif option == "3":
            print("\nUpdate Stock")

            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)

            if product is not None:
                print("Product Found:")
                print(f"Name: {product.name}")
                print(f"Current Stock: {product.stock}")

                try:
                    new_stock = int(input("New Stock Quantity: "))
                    product.update_stock(new_stock)
                    print("Stock updated successfully!")
                except ValueError:
                    print("Stock must be a non-negative integer.")

            else:
                print("Product not found.")

        elif option == "4":
            print("\nSearch Product")

            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)

            if product is not None:
                print("Product Found")
                print("-" * 48)
                product.display_information()
                print("-" * 48)
            else:
                print("Product not found.")

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()