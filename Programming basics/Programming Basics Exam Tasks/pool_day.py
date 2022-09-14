import math

people = int(input())
taks = float(input())
sun_lounger_price = float(input())
umbrella_price = float(input())
all_taks = people * taks
umbrella = math.ceil(people * 0.5) * umbrella_price
sun_lounger = math.ceil(people * 0.75) * sun_lounger_price
print(f"{all_taks + umbrella + sun_lounger:.2f} lv.")
