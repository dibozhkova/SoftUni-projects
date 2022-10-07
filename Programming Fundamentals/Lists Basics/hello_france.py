items = input().split("|")
budget = float(input())
buying_items = []
for el in items:
    item, price = el.split("->")
    price = float(price)
    if budget < price:
        continue
    if item == "Clothes" and price <= 50:
        budget -= price
        buying_items.append(price)
    elif item == "Shoes" and price <= 35:
        budget -= price
        buying_items.append(price)
    elif item == "Accessories" and price <= 20.5:
        budget -= price
        buying_items.append(price)
new_buying_items_price = ([el*1.4 for el in buying_items])
format_new_buying_item_price = (["%.2f" % el for el in new_buying_items_price])
print(*format_new_buying_item_price)
profit = sum(new_buying_items_price) - sum(buying_items)
print(f"Profit: {profit:.2f}")
new_budget = sum(new_buying_items_price) + budget
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
