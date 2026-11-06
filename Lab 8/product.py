from abc import ABC, abstractmethod
from supplier import Supplier

# Create Product class
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
             stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__supplier: Supplier = supplier

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self):
        return self.__stock

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )
        print(f"Supplier: {self.__supplier.name}")
        print(f"Supplier Email: {self.__supplier.contact_email}")

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass