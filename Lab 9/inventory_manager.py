import json
import os
from product import Product
from can_be_shipped import CanBeShipped
from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier

# Save Product objects to JSON
def save_inventory(inventory) -> None:
    print("Saving inventory...")

    data = []

    for product in inventory.get_products():
        data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")

# Load JSON data as the correct product subclasses

def load_inventory(inventory: Inventory) -> None:
    if not os.path.exists("inventory.json"):
        print("inventory.json not found.")
        return

    print("inventory.json found.")

    with open("inventory.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Keep one Supplier object for each Supplier ID
    suppliers: dict[str, Supplier] = {}

    for item in data:
        # Support old Lab 7 JSON records without suppliers
        supplier_data = item.get("supplier") or {
            "supplier_id": "S000",
            "name": "Unassigned Supplier",
            "contact_email": ""
        }

        supplier_id = supplier_data["supplier_id"]

        if supplier_id not in suppliers:
            suppliers[supplier_id] = Supplier(
                supplier_id,
                supplier_data["name"],
                supplier_data["contact_email"]
            )

        supplier = suppliers[supplier_id]

        # Ask the factory to create the correct product.
        product = ProductFactory.create(
            product_type=item.get("type", ""),
            product_id=item["id"],
            name=item["name"],
            price=item["price"],
            stock_quantity=item["stock"],
            supplier=supplier,
            weight=item.get("weight", 1.0),
            download_size=item.get("download_size", 1.0)
        )

        inventory.add_product(product)

    print("Inventory loaded successfully.")

# Display menu for user 
def main() -> None:
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

            if not product_id or not name or price <= 0 or stock < 0:
                print("Invalid product details.")
                continue


            # Ask for the supplier
            supplier_id = input("Supplier ID: ").strip()

            if not supplier_id:
                print("Supplier ID cannot be empty.")
                continue

            # Check if supplier already exists
            supplier = next(
                (p.supplier for p in inventory.get_products()
                if p.supplier.supplier_id == supplier_id),
                None
            )

            if supplier is None:
                supplier_name = input("Supplier Name: ").strip()
                supplier_email = input("Supplier Email: ").strip()

                if not supplier_name:
                    print("Supplier Name cannot be empty.")
                    continue

                supplier = Supplier(
                    supplier_id,
                    supplier_name,
                    supplier_email
                )
            else:
                print(f"Using existing supplier: {supplier.name}")

            try:
                if product_type == "1":
                    weight = float(input("Weight (kg): "))

                    if weight <= 0:
                        print("Weight must be greater than zero.")
                        continue

                    new_product = ProductFactory.create(
                        product_type="physical",
                        product_id=product_id,
                        name=name,
                        price=price,
                        stock_quantity=stock,
                        supplier=supplier,
                        weight=weight
                    )

                elif product_type == "2":
                    download_size = float(
                        input("Download Size (MB): ")
                    )

                    if download_size <= 0:
                        print(
                            "Download size must be greater than zero."
                        )
                        continue

                    new_product = ProductFactory.create(
                        product_type="digital",
                        product_id=product_id,
                        name=name,
                        price=price,
                        stock_quantity=stock,
                        supplier=supplier,
                        download_size=download_size
                    )

            except ValueError as error:
                print(f"Could not add product: {error}")
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