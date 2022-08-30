budget = int(input())
season = input()
num_of_fisherman = int(input())
price_for_boat = 0
if season == "Spring":
    if num_of_fisherman <= 6:
        price_for_boat = 3000 - (3000 * 0.1)
    elif 7 < num_of_fisherman <= 11:
        price_for_boat = 3000 - (3000 * 0.15)
    elif num_of_fisherman > 12:
        price_for_boat = 3000 - (3000 * 0.25)
elif season == "Summer" or season == "Autumn":
    if num_of_fisherman <= 6:
        price_for_boat = 4200 - (4200 * 0.1)
    elif 7 < num_of_fisherman <= 11:
        price_for_boat = 4200 - (4200 * 0.15)
    elif num_of_fisherman > 12:
        price_for_boat = 4200 - (4200 * 0.25)
elif season == "Winter":
    if num_of_fisherman <= 6:
        price_for_boat = 2600 - (2600 * 0.1)
    elif 7 < num_of_fisherman <= 11:
        price_for_boat = 2600 - (2600 * 0.15)
    elif num_of_fisherman > 12:
        price_for_boat = 2600 - (2600 * 0.25)
if num_of_fisherman % 2 == 0:
    if season != "Autumn":
        price_for_boat = price_for_boat - (price_for_boat * 0.05)
    else:
        price_for_boat = price_for_boat
if budget >= price_for_boat:
    print(f"Yes! You have {budget - price_for_boat:.2f} leva left.")
else:
    print(f"Not enough money! You need {price_for_boat - budget:.2f} leva.")
