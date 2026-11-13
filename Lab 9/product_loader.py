import csv

from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        loaded = 0

        with file:
            reader = csv.reader(file)

            # Skip the header.
            next(reader, None)

            # Header is row 1, so data begins at row 2.
            for row_number, row in enumerate(reader, start=2):
                try:
                    (
                        product_type,
                        product_id,
                        name,
                        price_text,
                        stock_text
                    ) = row

                    try:
                        price = float(price_text)
                    except ValueError:
                        raise ValueError(
                            "Price must be a number."
                        ) from None

                    try:
                        stock = int(stock_text)
                    except ValueError:
                        raise ValueError(
                            "Stock must be a whole number."
                        ) from None

                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=product_id,
                        name=name,
                        price=price,
                        stock_quantity=stock,
                        supplier=supplier
                    )

                    if inventory.add_product(product):
                        loaded += 1
                    else:
                        print(
                            f"Row {row_number} skipped: "
                            f"Duplicate product ID: {product_id}"
                        )

                except ValueError as error:
                    print(
                        f"Row {row_number} skipped: {error}"
                    )

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")