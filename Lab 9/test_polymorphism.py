
from product import Product
from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory


# A function that accepts any Product subclass
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# Create a Supplier
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

# Create an Inventory
inventory = Inventory()

# Add both product types into the same Inventory
inventory.add_product(physical)
inventory.add_product(digital)

# Test polymorphism using one loop
print("\nTesting Polymorphism")
print("-" * 48)

for product in inventory.get_products():
    show_product_details(product)
    print("-" * 48)

# Verify the correct subclass behaviour
assert physical.get_fulfilment_info() == (
    "This product requires physical shipping."
)

assert digital.get_fulfilment_info() == (
    "This product is delivered digitally through a download."
)

assert len(inventory.get_products()) == 2

print("\nAll polymorphism tests passed!")
