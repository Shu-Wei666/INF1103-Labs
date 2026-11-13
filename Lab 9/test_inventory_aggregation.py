
from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory

# Create a Supplier
supplier = Supplier("S001", "ABC Supplies", "sales@example.com")

product = ProductFactory.create(
    "physical",
    "P001",
    "Mouse",
    50.0,
    10,
    supplier,
    weight=0.5
)

# Create two inventories
inventory_a = Inventory()
inventory_b = Inventory()

# Step 1: Add product to Inventory A
print("\nStep 1: Add product to Inventory A")
inventory_a.add_product(product)
inventory_a.display_all()

# Step 2: Remove product from Inventory A
print("\nStep 2: Remove product from Inventory A")
inventory_a.remove_product("P001")
inventory_a.display_all()

# Step 3: Check whether product still exists
print("\nStep 3: Product still exists")
product.display_information()

# Step 4: Add the same product to Inventory B
print("\nStep 4: Add product to Inventory B")
inventory_b.add_product(product)
inventory_b.display_all()

# Step 5: Verify it is the same object
print("\nStep 5: Check object identity")
print(inventory_b.find_product("P001") is product)
