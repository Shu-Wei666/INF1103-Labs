from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

# PhysicalProduct inherits from Product and CanBeShipped
class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id: str, name: str, price: float,
             stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = float(weight)

    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_rate = 2.0
        return self.__weight * shipping_rate

    def to_dict(self) -> dict[str, str | float | int]:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data