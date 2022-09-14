drink = input()
sugar = input()
num_drinks = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = num_drinks * 0.9
    elif sugar == "Normal":
        price = num_drinks * 1
    elif sugar == "Extra":
        price = num_drinks * 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price = num_drinks * 1
    elif sugar == "Normal":
        price = num_drinks * 1.2
    elif sugar == "Extra":
        price = num_drinks * 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = num_drinks * 0.5
    elif sugar == "Normal":
        price = num_drinks * 0.6
    elif sugar == "Extra":
        price = num_drinks * 0.7

if sugar == "Without":
    price *= 0.65
if drink == "Espresso" and num_drinks >= 5:
    price *= 0.75
if price > 15:
    price *= 0.8
print(f"You bought {num_drinks} cups of {drink} for {price:.2f} lv.")
