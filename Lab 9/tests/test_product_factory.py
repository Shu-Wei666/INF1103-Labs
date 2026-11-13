import unittest

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory
from supplier import Supplier


class TestProductFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(
            "S001",
            "ABC Supplies",
            "sales@example.com"
        )

    def test_create_physical_product(self) -> None:
        product = ProductFactory.create(
            "physical",
            "P001",
            "Mouse",
            50.0,
            10,
            self.supplier,
            weight=0.5
        )

        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.product_id, "P001")
        self.assertAlmostEqual(product.price, 50.0)
        self.assertEqual(product.stock, 10)
        self.assertAlmostEqual(product.weight, 0.5)
        self.assertIs(product.supplier, self.supplier)

    def test_create_digital_product(self) -> None:
        product = ProductFactory.create(
            "digital",
            "D001",
            "Game",
            80.0,
            30,
            self.supplier,
            download_size=1500.0
        )

        self.assertIsInstance(product, DigitalProduct)
        self.assertAlmostEqual(product.download_size, 1500.0)
        self.assertIs(product.supplier, self.supplier)

    def test_products_support_common_base_type(self) -> None:
        for product_type in ("physical", "digital"):
            with self.subTest(product_type=product_type):
                product = ProductFactory.create(
                    product_type,
                    "T001",
                    "Test Product",
                    10.0,
                    5,
                    self.supplier
                )

                self.assertIsInstance(product, Product)

    def test_defaults_for_lab_csv(self) -> None:
        physical = ProductFactory.create(
            "physical",
            "P002",
            "Lamp",
            25.0,
            10,
            self.supplier
        )

        digital = ProductFactory.create(
            "digital",
            "D002",
            "Editor",
            49.90,
            100,
            self.supplier
        )

        self.assertAlmostEqual(physical.weight, 1.0)
        self.assertAlmostEqual(digital.download_size, 1.0)

    def test_unknown_product_type(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "^Unknown product type: service$"
        ):
            ProductFactory.create(
                "service",
                "S001",
                "Installation",
                30.0,
                5,
                self.supplier
            )


if __name__ == "__main__":
    unittest.main()