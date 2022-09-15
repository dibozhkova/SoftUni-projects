budget = float(input())
statist = int(input())
clothing_price = float(input())
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
decor = budget * 0.1
all_clothing = statist * clothing_price
if statist > 150:
    all_clothing = all_clothing - all_clothing * 0.1
total_sum = decor + all_clothing
if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - budget:.2f} leva more.")
if total_sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_sum:.2f} leva left.")
