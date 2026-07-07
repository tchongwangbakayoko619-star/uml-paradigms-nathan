# Imperative / Procedural Version

def calculate_cart_total(products):
    """Calculate the total price of a shopping cart with a 10% discount if the total exceeds 50,000 FCFA."""
    total = 0

    for product in products:
        total += product["unit_price"] * product["quantity"]

    # Apply discount
    if total > 50000:
        total *= 0.9

    return total


# Example usage
if __name__ == "__main__":
    shopping_cart = [
        {"name": "Python Book", "unit_price": 25000, "quantity": 2},
        {"name": "Notebook", "unit_price": 2000, "quantity": 5,
    ]

    print("Imperative Total:", calculate_cart_total(shopping_cart), "FCFA")
