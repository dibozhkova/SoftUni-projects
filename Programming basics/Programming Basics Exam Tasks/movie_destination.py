film_budget = float(input())
destination = input()
season = input()
num_days = int(input())
price = 0
if season == "Winter":
    if destination == "Dubai":
        price = 45000 * 0.7
    elif destination == "Sofia":
        price = 17000 * 1.25
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000 * 0.7
    elif destination == "Sofia":
        price = 12500 * 1.25
    elif destination == "London":
        price = 20250
total_price = price * num_days
diff = abs(film_budget - total_price)
if film_budget >= total_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
