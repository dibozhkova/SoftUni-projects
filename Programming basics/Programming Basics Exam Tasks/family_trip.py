budget = float(input())
number_nights = int(input())
price_night = float(input())
extra_expenses = int(input())
all_budget = budget - budget * (extra_expenses / 100)
if number_nights > 7:
    price_night = price_night - (price_night * 0.05)
all_price = number_nights * price_night
if all_budget >= all_price:
    print(f"Ivanovi will be left with {all_budget - all_price:.2f} leva after vacation.")
else:
    print(f"{all_price - all_budget:.2f} leva needed.")
