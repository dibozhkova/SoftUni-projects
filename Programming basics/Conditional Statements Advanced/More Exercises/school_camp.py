season = input()
type_of_group = input()
num_of_students = int(input())
num_of_nights = int(input())
type_of_sport = ""
price_for_night = 0
if season == "Winter":
    if type_of_group == "girls"\
        or type_of_group == "boys":
        price_for_night = 9.6
    elif type_of_group == "mixed":
        price_for_night = 10
elif season == "Spring":
    if type_of_group == "girls"\
        or type_of_group == "boys":
        price_for_night = 7.2
    elif type_of_group == "mixed":
        price_for_night = 9.5
elif season == "Summer":
    if type_of_group == "girls"\
        or type_of_group == "boys":
        price_for_night = 15
    elif type_of_group == "mixed":
        price_for_night = 20
total_price_for_nights = num_of_students * num_of_nights * price_for_night
if num_of_students >= 50:
    total_price_for_nights = total_price_for_nights / 2
elif 20 <= num_of_students < 50:
    total_price_for_nights = total_price_for_nights - (total_price_for_nights * 0.15)
elif 10 <= num_of_students < 20:
    total_price_for_nights = total_price_for_nights - (total_price_for_nights * 0.05)
if season == "Winter":
    if type_of_group == "girls":
        type_of_sport = "Gymnastics"
    elif type_of_group == "boys":
        type_of_sport = "Judo"
    elif type_of_group == "mixed":
        type_of_sport = "Ski"
elif season == "Spring":
    if type_of_group == "girls":
        type_of_sport = "Athletics"
    elif type_of_group == "boys":
        type_of_sport = "Tennis"
    elif type_of_group == "mixed":
        type_of_sport = "Cycling"
elif season == "Summer":
    if type_of_group == "girls":
        type_of_sport = "Volleyball"
    elif type_of_group == "boys":
        type_of_sport = "Football"
    elif type_of_group == "mixed":
        type_of_sport = "Swimming"
print(f"{type_of_sport} {total_price_for_nights:.2f} lv.")
