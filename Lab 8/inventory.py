from product import Product

# Inventory class manages a collection of Product objects
class Inventory:

    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product):
        if self.find_product(product.product_id) is not None:
            return False

        self.__products.append(product)
        return True

    def remove_product(self, product_id: str):
        for product in self.__products:
            if product.product_id == product_id:
                self.__products.remove(product)
                return True

        return False

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product

        return None

    # Keep the existing method for inventory_manager.py
    def search_product(self, product_id: str):
        return self.find_product(product_id)

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 48)

        if not self.__products:
            print("No products in inventory.")
        else:
            for product in self.__products:
                product.display_information()

        print("-" * 48)

    def get_products(self) -> list[Product]:
        return self.__products.copy()
