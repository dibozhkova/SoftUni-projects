num_of_day_for_trip = int(input())
type_of_room = input()
rating = input()
price_one_overnight = 0
if type_of_room == "room for one person":
    price_one_overnight = 18
elif type_of_room == "apartment":
    if num_of_day_for_trip < 10:
        price_one_overnight = 25 - (25 * 0.3)
    elif 10 < num_of_day_for_trip < 15:
        price_one_overnight = 25 - (25 * 0.35)
    elif num_of_day_for_trip > 15:
        price_one_overnight = 25 - (25 * 0.5)
elif type_of_room == "president apartment":
    if num_of_day_for_trip < 10:
        price_one_overnight = 35 - (35 * 0.1)
    elif 10 < num_of_day_for_trip < 15:
        price_one_overnight = 35 - (35 * 0.15)
    elif num_of_day_for_trip > 15:
        price_one_overnight = 35 - (35 * 0.2)
total_sum = price_one_overnight * (num_of_day_for_trip - 1)
if rating == "positive":
    total_sum = total_sum + (total_sum * 0.25)
elif rating == "negative":
    total_sum = total_sum - (total_sum * 0.1)
print(f"{total_sum:.2f}")