budget = float(input())
season = input()
type_of_car = ""
class_of_car = ""
rent = 0
if budget <= 100:
    class_of_car = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        rent = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        rent = budget * 0.65
elif 100 < budget <= 500:
    class_of_car = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        rent = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        rent = budget * 0.8
elif budget > 500:
    class_of_car = "Luxury class"
    if season == "Summer"\
        or season == "Winter":
        type_of_car = "Jeep"
        rent = budget * 0.9
print(class_of_car)
print(f"{type_of_car} - {rent:.2f}")
