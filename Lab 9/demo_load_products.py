from inventory import Inventory
from supplier import Supplier
from product_loader import load_products


def main() -> None:
    supplier = Supplier(
        "S001",
        "ABC Supplies",
        "sales@example.com"
    )

    inventory = Inventory()

    load_products(
        "products.csv",
        inventory,
        supplier
    )

    print("\nProducts currently in inventory:")
    inventory.display_all()


if __name__ == "__main__":
    main()