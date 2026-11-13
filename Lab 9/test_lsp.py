
from product import Product
from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory


# Function accepts the parent class Product
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# Create Supplier
supplier = Supplier("S001", "ABC Supplies", "sales@example.com")

physical = ProductFactory.create(
    "physical",
    "P001",
    "Mouse",
    50.0,
    10,
    supplier,
    weight=0.5
)

digital = ProductFactory.create(
    "digital",
    "D001",
    "Game",
    80.0,
    30,
    supplier,
    download_size=1500.0
)

# Test 1: Pass PhysicalProduct to the same function
print("\nTest 1: PhysicalProduct")
show_product_details(physical)

# Test 2: Pass DigitalProduct to the same function
print("\nTest 2: DigitalProduct")
show_product_details(digital)

# Test 3: Update stock for both types
print("\nTest 3: Update Stock")

physical.update_stock(20)
digital.update_stock(40)

print(f"Physical Product Stock: {physical.stock}")
print(f"Digital Product Stock: {digital.stock}")

# Test 4: Add both types to Inventory
print("\nTest 4: Inventory")

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)

for product in inventory.get_products():
    show_product_details(product)

# Check that both products work correctly
assert physical.stock == 20
assert digital.stock == 40
assert inventory.find_product("P001") is physical
assert inventory.find_product("D001") is digital

print("\nAll LSP tests passed!")
