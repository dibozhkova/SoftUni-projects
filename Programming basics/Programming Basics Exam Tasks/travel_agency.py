city = input()
package = input()
vip = input()
days = int(input())
price = 0
invalid_input = False
if city == "Bansko" or city == "Borovets":
    if package == "withEquipment":
        price = 100
        if vip == "yes":
            price *= 0.9
        elif vip == "no":
            price = price
    elif package == "noEquipment":
        price = 80
        if vip == "yes":
            price *= 0.95
        elif vip == "no":
            price = price
    else:
        invalid_input = True
elif city == "Varna" or city == "Burgas":
    if package == "withBreakfast":
        price = 130
        if vip == "yes":
            price *= 0.88
        elif vip == "no":
            price = price
    elif package == "noBreakfast":
        price = 100
        if vip == "yes":
            price *= 0.93
        elif vip == "no":
            price = price
    else:
        invalid_input = True
else:
    invalid_input = True
total_price = price * days
if days > 7:
    total_price -= price
# elif days < 1:
#     print("Days must be positive number!")
if invalid_input:
    print("Invalid input!")
elif days < 1:
    print("Days must be positive number!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
