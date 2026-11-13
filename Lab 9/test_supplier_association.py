from supplier import Supplier
from product_factory import ProductFactory

# Create a Supplier independently
supplier = Supplier("S001", "ABC Supplies", "sales@example.com")

# Create products associated with the same Supplier
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

print("Before deleting supplier variable:")
physical.display_information()
digital.display_information()

# Delete the original variable
del supplier

print("\nAfter deleting supplier variable:")
physical.display_information()
digital.display_information()

print("\nBoth products share the same supplier:",
      physical.supplier is digital.supplier)
