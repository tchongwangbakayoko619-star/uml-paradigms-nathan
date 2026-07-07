# Object-Oriented Version

class Product:
    def __init__(self, name, unit_price, quantity):
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def get_subtotal(self):
        return self.unit_price * self.quantity


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total(self):
        total = sum(product.get_subtotal() for product in self.products)

        # Apply 10% discount
        if total > 50000:
            total *= 0.9

        return total


# Example usage
if __name__ == "__main__":
    cart = Cart()
    cart.add_product(Product("Python Book", 25000, 2))
    cart.add_product(Product("Notebook", 2000, 5))

    print("OOP Total:", cart.get_total(), "FCFA")
