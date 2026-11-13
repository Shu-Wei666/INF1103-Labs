import io
import tempfile
import unittest

from contextlib import redirect_stdout
from pathlib import Path

from inventory import Inventory
from product_loader import load_products
from supplier import Supplier


SAMPLE_CSV = (
    "product_type,product_id,name,price,stock_quantity\n"
    "physical,P001,Desk Lamp,25.00,10\n"
    "digital,D001,Photo Editor,49.90,100\n"
    "service,S001,Installation,30.00,5\n"
    "physical,P002,Office Chair,abc,3\n"
    "physical,P003,Monitor Stand,39.50,7\n"
)


class TestProductLoader(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(
            "S001",
            "ABC Supplies",
            "sales@example.com"
        )
        self.inventory = Inventory()

    def test_valid_rows_load_and_bad_rows_are_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "products.csv"
            path.write_text(SAMPLE_CSV, encoding="utf-8")

            output = io.StringIO()

            with redirect_stdout(output):
                load_products(
                    str(path),
                    self.inventory,
                    self.supplier
                )

        self.assertEqual(
            len(self.inventory.get_products()),
            3
        )

        for product_id in ("P001", "D001", "P003"):
            self.assertIsNotNone(
                self.inventory.find_product(product_id)
            )

        self.assertIsNone(
            self.inventory.find_product("S001")
        )
        self.assertIsNone(
            self.inventory.find_product("P002")
        )

        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Row 4 skipped: Unknown product type: service",
                "Row 5 skipped: Price must be a number.",
                "3 products loaded.",
                "Load attempt finished."
            ]
        )

    def test_missing_file_is_handled(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "missing.csv"
            output = io.StringIO()

            with redirect_stdout(output):
                load_products(
                    str(path),
                    self.inventory,
                    self.supplier
                )

        self.assertEqual(
            len(self.inventory.get_products()),
            0
        )

        self.assertEqual(
            output.getvalue().splitlines(),
            [
                f"Products file not found: {path}",
                "Load attempt finished."
            ]
        )

    def test_validation_failure_does_not_stop_later_rows(self) -> None:
        data = (
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P001,Bad Price,0,10\n"
            "digital,D001,Bad Stock,20,-1\n"
            "physical,P002,Valid Product,15,3\n"
        )

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "products.csv"
            path.write_text(data, encoding="utf-8")

            output = io.StringIO()

            with redirect_stdout(output):
                load_products(
                    str(path),
                    self.inventory,
                    self.supplier
                )

        self.assertEqual(
            len(self.inventory.get_products()),
            1
        )
        self.assertIsNotNone(
            self.inventory.find_product("P002")
        )

        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Row 2 skipped: Price must be greater than zero.",
                "Row 3 skipped: Stock cannot be negative.",
                "1 products loaded.",
                "Load attempt finished."
            ]
        )


if __name__ == "__main__":
    unittest.main()