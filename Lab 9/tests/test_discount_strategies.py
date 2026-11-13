import unittest

from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


class TestDiscountStrategies(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(
            "S001",
            "ABC Supplies",
            "sales@example.com"
        )

        self.product = PhysicalProduct(
            "P001",
            "Desk",
            125.0,
            10,
            5.0,
            self.supplier
        )

    def make_order(self, discount=None) -> Order:
        order = Order("O001", discount)
        order.add_order_line(self.product, 2)
        return order

    def test_default_no_discount(self) -> None:
        order = self.make_order()
        self.assertAlmostEqual(order.calculate_total(), 250.0)

    def test_explicit_no_discount(self) -> None:
        order = self.make_order(NoDiscount())
        self.assertAlmostEqual(order.calculate_total(), 250.0)

    def test_percentage_discount(self) -> None:
        order = self.make_order(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225.0)

    def test_bulk_discount_above_threshold(self) -> None:
        order = self.make_order(BulkDiscount(200, 20))
        self.assertAlmostEqual(order.calculate_total(), 230.0)

    def test_bulk_discount_at_threshold(self) -> None:
        strategy = BulkDiscount(200, 20)
        self.assertAlmostEqual(strategy.apply(200), 180.0)

    def test_bulk_discount_below_threshold(self) -> None:
        order = Order("O002", BulkDiscount(200, 20))
        order.add_order_line(self.product, 1)

        self.assertAlmostEqual(order.calculate_total(), 125.0)

    def test_change_existing_order_discount(self) -> None:
        order = self.make_order(BulkDiscount(200, 20))
        self.assertAlmostEqual(order.calculate_total(), 230.0)

        order.set_discount(PercentageDiscount(10))

        self.assertAlmostEqual(order.calculate_total(), 225.0)

    def test_student_discount(self) -> None:
        order = self.make_order(StudentDiscount())
        self.assertAlmostEqual(order.calculate_total(), 237.5)

    def test_two_orders_share_one_strategy(self) -> None:
        strategy = PercentageDiscount(10)

        first = self.make_order(strategy)
        second = self.make_order(strategy)

        self.assertIs(first.discount, second.discount)
        self.assertAlmostEqual(first.calculate_total(), 225.0)
        self.assertAlmostEqual(second.calculate_total(), 225.0)


if __name__ == "__main__":
    unittest.main()