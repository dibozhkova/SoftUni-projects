budget = float(input())
season = input()
destination = ""
holiday_expense = 0
plays_to_stay = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        holiday_expense = budget * 0.3
        plays_to_stay = "Camp"
    elif season == "winter":
        holiday_expense = budget * 0.7
        plays_to_stay = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        holiday_expense = budget * 0.4
        plays_to_stay = "Camp"
    elif season == "winter":
        holiday_expense = budget * 0.8
        plays_to_stay = "Hotel"
else:
    destination = "Europe"
    plays_to_stay = "Hotel"
    holiday_expense = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{plays_to_stay} - {holiday_expense:.2f}")