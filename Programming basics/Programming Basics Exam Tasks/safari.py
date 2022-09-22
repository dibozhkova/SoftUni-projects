budget = float(input())
fuel_need_l = float(input())
day = input()
# •	Цената на един литър гориво е 2.10 лв.
# •	Цената за екскурзовод е 100лв.
# •	В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%
all_fuel = fuel_need_l * 2.10
all_sum = all_fuel + 100
if day == "Saturday":
    all_sum = all_sum - all_sum * 0.1
elif day == "Sunday":
    all_sum = all_sum - all_sum * 0.2
else:
    all_sum = all_sum
if budget >= all_sum:
    print(f"Safari time! Money left: {budget - all_sum:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {all_sum - budget:.2f} lv.")
