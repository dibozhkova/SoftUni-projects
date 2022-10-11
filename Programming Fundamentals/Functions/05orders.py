# Write a function that calculates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are: 
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00

# Print the result formatted to the second decimal place.


def calculate(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "water":
        return quantity
    elif product == "coke":
        return quantity * 1.4
    elif product == "snacks":
        return quantity * 2

product_input = input()
quantity_input = int(input())
total_price = calculate(product_input, quantity_input)
print(f"{total_price:.2f}")
