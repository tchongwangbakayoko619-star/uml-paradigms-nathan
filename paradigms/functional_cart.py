# Functional Version (Pure Functions + map/reduce)

from functools import reduce


def calculate_subtotal(product):
    """Pure function that calculates the subtotal of a product."""
    return product["unit_price"] * product["quantity"]


def calculate_cart_total(products):
    """Calculate the shopping cart total using map and reduce."""
    subtotals = map(calculate_subtotal, products)
    total = reduce(lambda x, y: x + y, subtotals, 0)

    # Apply 10% discount
    if total > 50000:
        total *= 0.9

    return total


# Example usage
if __name__ == "__main__":
    shopping_cart = [
        {"name": "Python Book", "unit_price": 25000, "quantity": 2},
        {"name": "Notebook", "unit_price": 2000, "quantity": 5},
    ]

    print("Functional Total:", calculate_cart_total(shopping_cart), "FCFA")
