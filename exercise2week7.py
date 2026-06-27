class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_shipping_info(self):
        return "Shipping info not defined"

    def describe(self):
        print(f"Product: {self.name}, Price: ${self.price:.2f}")


class PhysicalProduct(Product):
    def __init__(self, name, price, weight_kg):
        super().__init__(name, price)
        self.weight_kg = weight_kg

    def get_shipping_info(self):
        return f"Ships in 3–5 days. Weight: {self.weight_kg} kg"


class DigitalProduct(Product):
    def __init__(self, name, price, file_size_mb):
        super().__init__(name, price)
        self.file_size_mb = file_size_mb

    def get_shipping_info(self):
        return f"Instant download. Size: {self.file_size_mb} MB"


if __name__ == "__main__":
    products = [
        PhysicalProduct("Headphones", 45.00, 2.5),
        DigitalProduct("Ebook", 12.99, 150)
    ]

    for product in products:
        product.describe()
        print(product.get_shipping_info())
        print()
