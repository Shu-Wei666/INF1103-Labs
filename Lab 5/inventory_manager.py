import json
import os
inventory = []
def load_inventory():
    global inventory

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")

    else:
        print("inventory.json not found.")
        inventory = []
# Loop through the list and display every product in the list
def display_all():
    print("\nCurrent Inventory")
    print("-" * 48)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 48)
# Allow user to add products
def add_product():
    print("\nAdd New Product")

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)
    print("Product added successfully!")
# Allow user to update the stock quantity
def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return
    print("Product not found.")
# Allow user to search for products and display them
def search_product():
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("-" * 48)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 48)
            return
    print("Product not found.")
load_inventory()
display_all()