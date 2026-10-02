inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]

print(inventory)
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
display_all()
update_stock()
display_all()