import unittest

from supplier import Supplier
from product_factory import ProductFactory
from order_line import OrderLine


class TestValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(
            "S001",
            "ABC Supplies",
            "sales@example.com"
        )

    def make_product(
        self,
        product_type="physical",
        price=50.0,
        stock=10
    ):
        return ProductFactory.create(
            product_type=product_type,
            product_id="P001",
            name="Test Product",
            price=price,
            stock_quantity=stock,
            supplier=self.supplier
        )

    def test_zero_price_rejected(self) -> None:
        for product_type in ("physical", "digital"):
            with self.subTest(product_type=product_type):
                with self.assertRaisesRegex(
                    ValueError,
                    "Price must be greater than zero"
                ):
                    self.make_product(
                        product_type=product_type,
                        price=0
                    )

    def test_negative_price_rejected(self) -> None:
        for product_type in ("physical", "digital"):
            with self.subTest(product_type=product_type):
                with self.assertRaisesRegex(
                    ValueError,
                    "Price must be greater than zero"
                ):
                    self.make_product(
                        product_type=product_type,
                        price=-5
                    )

    def test_positive_price_accepted(self) -> None:
        product = self.make_product(price=12.50)

        self.assertAlmostEqual(product.price, 12.50)

    def test_negative_initial_stock_rejected(self) -> None:
        for product_type in ("physical", "digital"):
            with self.subTest(product_type=product_type):
                with self.assertRaisesRegex(
                    ValueError,
                    "Stock cannot be negative"
                ):
                    self.make_product(
                        product_type=product_type,
                        stock=-1
                    )

    def test_zero_initial_stock_accepted(self) -> None:
        product = self.make_product(stock=0)

        self.assertEqual(product.stock, 0)

    def test_negative_stock_update_preserves_stock(self) -> None:
        for product_type in ("physical", "digital"):
            with self.subTest(product_type=product_type):
                product = self.make_product(
                    product_type=product_type,
                    stock=10
                )

                with self.assertRaisesRegex(
                    ValueError,
                    "Stock cannot be negative"
                ):
                    product.update_stock(-1)

                self.assertEqual(product.stock, 10)

    def test_update_stock_to_zero(self) -> None:
        product = self.make_product(stock=10)

        product.update_stock(0)

        self.assertEqual(product.stock, 0)

    def test_zero_order_quantity_rejected(self) -> None:
        product = self.make_product()

        with self.assertRaisesRegex(
            ValueError,
            "Quantity must be greater than zero"
        ):
            OrderLine(product, 0)

    def test_negative_order_quantity_rejected(self) -> None:
        product = self.make_product()

        with self.assertRaisesRegex(
            ValueError,
            "Quantity must be greater than zero"
        ):
            OrderLine(product, -2)

    def test_positive_order_quantity_accepted(self) -> None:
        product = self.make_product(price=50.0)

        line = OrderLine(product, 2)

        self.assertEqual(line.quantity, 2)
        self.assertAlmostEqual(
            line.calculate_subtotal(),
            100.0
        )


if __name__ == "__main__":
    unittest.main()