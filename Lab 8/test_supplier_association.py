
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# Create a Supplier independently
supplier = Supplier("S001", "ABC Supplies", "sales@example.com")

# Create products associated with the same Supplier
physical = PhysicalProduct("P001", "Mouse", 50.0, 10, 0.5, supplier)
digital = DigitalProduct("D001", "Game", 80.0, 30, 1500.0, supplier)

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
