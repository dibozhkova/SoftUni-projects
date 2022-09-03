lylis_age = int(input())
wachmashine_price = float(input())
toy_price = int(input())

toy_num = 0
money_for_odd_bt = 10
total_sum = 0
brother_count = 0
for birthdays in range(1, lylis_age + 1):
    if birthdays % 2 != 0:
        toy_num = toy_num + 1
    else:
        brother_count = brother_count + 1
        total_sum = total_sum + money_for_odd_bt
        money_for_odd_bt = money_for_odd_bt + 10

sold_toy = toy_num * toy_price
all_sum = total_sum + sold_toy - brother_count
if all_sum >= wachmashine_price:
    print(f"Yes! {all_sum - wachmashine_price:.2f}")
else:
    diff = abs(all_sum - wachmashine_price)
    print(f"No! {diff:.2f}")
