
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


# Create Supplier
supplier = Supplier("S001", "ABC Supplies", "sales@example.com")

# Create Products
mouse = PhysicalProduct(
    "P001", "Mouse", 50.0, 10, 0.5, supplier
)

game = DigitalProduct(
    "D001", "Game", 80.0, 30, 1500.0, supplier
)

# Create first Order
order1 = Order("O001")

# Add two products to Order 1
order1.add_order_line(mouse, 2)
order1.add_order_line(game, 1)

print("Step 1: Display Order 1")
order1.display_order()

# Create second Order using the same Mouse product
order2 = Order("O002")
order2.add_order_line(mouse, 3)

print("\nStep 2: Display Order 2")
order2.display_order()

# Check object identity
print("\nStep 3: Check object identity")

print(
    "Same Product object:",
    order1.order_lines[0].product is order2.order_lines[0].product
)

print(
    "Different OrderLine objects:",
    order1.order_lines[0] is not order2.order_lines[0]
)

# Remove Mouse from Order 1
print("\nStep 4: Remove Mouse from Order 1")
order1.remove_order_line("P001")
order1.display_order()

# Confirm Mouse Product still exists
print("\nStep 5: Mouse Product still exists")
mouse.display_information()
