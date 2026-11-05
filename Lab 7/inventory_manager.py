import json
import os
from product import Product
from can_be_shipped import CanBeShipped
from physical_product import PhysicalProduct

# DigitalProduct inherits from Product
class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = float(download_size)

    @property
    def download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB") 

    def get_fulfilment_info(self):
        return "This product is delivered digitally through a download."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data

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

# Load JSON data as the correct product subclasses
def load_inventory(inventory):
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product_type = item.get("type")

            if product_type == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"]
                )

            elif product_type == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                raise ValueError(
                    f"Unknown product type for ID {item['id']}: "
                    f"{product_type}. Update inventory.json."
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
            print("1. Physical Product")
            print("2. Digital Product")

            product_type = input("Select product type: ").strip()

            if product_type not in ("1", "2"):
                print("Invalid product type.")
                continue

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

            try:
                if product_type == "1":
                    weight = float(input("Weight (kg): "))

                    if weight <= 0:
                        print("Weight must be greater than zero.")
                        continue

                    new_product = PhysicalProduct(
                        product_id, name, price, stock, weight
                    )

                elif product_type == "2":
                    download_size = float(
                        input("Download Size (MB): ")
                    )

                    if download_size <= 0:
                        print("Download size must be greater than zero.")
                        continue

                    new_product = DigitalProduct(
                        product_id, name, price, stock, download_size
                    )

            except ValueError:
                print("Invalid weight or download size.")
                continue

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