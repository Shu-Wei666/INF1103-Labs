from abc import ABC, abstractmethod

# Interface for products that can be shipped
class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass