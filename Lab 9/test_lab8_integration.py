
import json
import os
import tempfile

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from inventory_manager import load_inventory, save_inventory


# Use a temporary directory so actual inventory.json is safe
original_dir = os.getcwd()

with tempfile.TemporaryDirectory() as temp_dir:
    try:
        os.chdir(temp_dir)

        # Test 1: Load old JSON without supplier details
        starter_data = [
            {
                "id": "P001",
                "name": "Mouse",
                "price": 50.0,
                "stock": 10,
                "type": "physical",
                "weight": 0.5
            },
            {
                "id": "D001",
                "name": "Game",
                "price": 80.0,
                "stock": 30,
                "type": "digital",
                "download_size": 1500.0
            }
        ]

        with open("inventory.json", "w", encoding="utf-8") as file:
            json.dump(starter_data, file)

        inventory = Inventory()
        load_inventory(inventory)

        assert len(inventory.get_products()) == 2
        assert inventory.find_product("P001").supplier.name == (
            "Unassigned Supplier"
        )

        print("Test 1 passed: Legacy JSON loaded")

        # Test 2: Add products with a shared Supplier
        supplier = Supplier(
            "S001", "ABC Supplies", "sales@example.com"
        )

        inventory.add_product(
            PhysicalProduct(
                "P002", "Keyboard", 90.0, 5, 1.0, supplier
            )
        )

        inventory.add_product(
            DigitalProduct(
                "D002", "App", 20.0, 3, 100.0, supplier
            )
        )

        assert len(inventory.get_products()) == 4
        print("Test 2 passed: Products added")

        # Test 3: Save and reload inventory
        save_inventory(inventory)

        reloaded = Inventory()
        load_inventory(reloaded)

        assert len(reloaded.get_products()) == 4

        physical = reloaded.find_product("P002")
        digital = reloaded.find_product("D002")

        assert physical.supplier.name == "ABC Supplies"
        assert physical.supplier is digital.supplier

        print("Test 3 passed: Save and reload")

        # Test 4: Check polymorphism
        assert digital.get_fulfilment_info() == (
            "This product is delivered digitally "
            "through a download."
        )

        print("Test 4 passed: Polymorphism")

        # Test 5: Check Order composition
        order = Order("O001")

        order.add_order_line(
            reloaded.find_product("P001"), 2
        )

        order.add_order_line(
            reloaded.find_product("D001"), 1
        )

        assert order.calculate_total() == 180.0
        print("Test 5 passed: Order total")

        print("\nAll Lab 8 integration checks passed!")

    finally:
        os.chdir(original_dir)
