number_of_orders = int(input())
total_price = 0
for orders in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price_for_coffee = price_per_capsule * days * capsules_per_day
    total_price += price_for_coffee
    print(f"The price for the coffee is: ${price_for_coffee:.2f}")
print(f"Total: ${total_price:.2f}")
