month = int(input())

electricity = 0
water = 0
internet = 0
others = 0

for bills in range(1, month + 1):
    electricity_sum = float(input())
    electricity = electricity + electricity_sum
    water = water + 20
    internet = internet + 15
    others = (electricity + water + internet) + (electricity + water + internet) * 0.2

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
average = (electricity + water + internet + others) / month
print(f"Average: {average:.2f} lv")
