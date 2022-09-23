num_days = int(input())
num_hours_per_day = int(input())
price = 0
for day in range(1, num_days + 1):
    price_per_day = 0
    for hour in range(1, num_hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price += 2.5
            price_per_day += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price += 1.25
            price_per_day += 1.25
        else:
            price += 1
            price_per_day += 1
    print(f"Day: {day} - {price_per_day:.2f} leva")
print(f"Total: {price:.2f} leva")
