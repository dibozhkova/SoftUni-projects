budget = float(input())
statist = int(input())
clothing = float(input())
decor = budget * 0.1
clothing_price = statist * clothing
if statist > 150:
    clothing_price = clothing_price * 0.9

total_sum = decor + clothing_price
if (decor + clothing_price) > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - total_sum):.2f} leva more.")
if decor + clothing_price <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_sum:.2f} leva left.")
# решена самостоятелно