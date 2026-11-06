from product import Product
from order_line import OrderLine

class Order:

    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total

    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.order_lines:
            if order_line.product.product_id == product_id:
                self.order_lines.remove(order_line)
                return True

        return False

    def display_order(self) -> None:
        print(f"\nOrder ID: {self.order_id}")
        print("-" * 48)

        for order_line in self.order_lines:
            print(
                f"Product: {order_line.product.name} | "
                f"Quantity: {order_line.quantity} | "
                f"Subtotal: ${order_line.calculate_subtotal():.2f}"
            )

        print("-" * 48)
        print(f"Order Total: ${self.calculate_total():.2f}")
