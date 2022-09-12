season = input()
km_for_month = float(input())
price_km = 0
if km_for_month <= 5000:
    if season == "Spring"\
        or season == "Autumn":
        price_km = 0.75
    elif season == "Summer":
        price_km = 0.9
    elif season == "Winter":
        price_km = 1.05
elif 5000 < km_for_month <= 10000:
    if season == "Spring"\
        or season == "Autumn":
        price_km = 0.95
    elif season == "Summer":
        price_km = 1.1
    elif season == "Winter":
        price_km = 1.25
elif 10000 < km_for_month <= 20000:
    price_km = 1.45
total_sum = km_for_month * 4 * price_km
driver_salary = total_sum - (total_sum * 0.1)
print(f"{driver_salary:.2f}")
