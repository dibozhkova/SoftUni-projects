budget = float(input())
number_of_serials = int(input())
total_price = 0
for serial in range(number_of_serials):
    name_serial = input()
    price_for_serial = float(input())
    if name_serial == "Thrones":
        price_for_serial /= 2
        total_price += price_for_serial
    elif name_serial == "Lucifer":
        price_for_serial *= 0.6
        total_price += price_for_serial
    elif name_serial == "Protector":
        price_for_serial *= 0.7
        total_price += price_for_serial
    elif name_serial == "TotalDrama":
        price_for_serial *= 0.8
        total_price += price_for_serial
    elif name_serial == "Area":
        price_for_serial *= 0.9
        total_price += price_for_serial
    else:
        total_price += price_for_serial
diff = abs(budget - total_price)
if budget >= total_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
