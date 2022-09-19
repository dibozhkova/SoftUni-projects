import math

num_guest = int(input())
budget = float(input())

eastern_bread_need = math.ceil(num_guest / 3)
eggs_need = num_guest * 2
price_eastern_bread = eastern_bread_need * 4
price_eggs = eggs_need * 0.45
total_price = price_eggs + price_eastern_bread
diff = abs(budget - total_price)
if budget >= total_price:
    print(f"Lyubo bought {eastern_bread_need} Easter bread and {eggs_need} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
