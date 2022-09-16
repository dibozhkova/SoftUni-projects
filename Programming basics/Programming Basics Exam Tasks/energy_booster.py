fruit = input()
size_set = input()
num_set_order = int(input())
price_set = 0
if size_set == "small":
    if fruit == "Watermelon":
        price_set = 2 * 56
    elif fruit == "Mango":
        price_set = 2 * 36.66
    elif fruit == "Pineapple":
        price_set = 2 * 42.10
    elif fruit == "Raspberry":
        price_set = 2 * 20
elif size_set == "big":
    if fruit == "Watermelon":
        price_set = 5 * 28.70
    elif fruit == "Mango":
        price_set = 5 * 19.60
    elif fruit == "Pineapple":
        price_set = 5 * 24.80
    elif fruit == "Raspberry":
        price_set = 5 * 15.20
final_price = num_set_order * price_set
if 400 <= final_price <= 1000:
    final_price = final_price * 0.85
elif final_price > 1000:
    final_price = final_price * 0.5
print(f"{final_price:.2f} lv.")
