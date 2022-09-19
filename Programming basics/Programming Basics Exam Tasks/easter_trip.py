destination = input()
date_for_trip = input()
num_nights = int(input())

if destination == "France":
    if date_for_trip == "21-23":
        num_nights *= 30
    elif date_for_trip == "24-27":
        num_nights *= 35
    elif date_for_trip == "28-31":
        num_nights *= 40
elif destination == "Italy":
    if date_for_trip == "21-23":
        num_nights *= 28
    elif date_for_trip == "24-27":
        num_nights *= 32
    elif date_for_trip == "28-31":
        num_nights *= 39
elif destination == "Germany":
    if date_for_trip == "21-23":
        num_nights *= 32
    elif date_for_trip == "24-27":
        num_nights *= 37
    elif date_for_trip == "28-31":
        num_nights *= 43
print(f"Easter trip to {destination} : {num_nights:.2f} leva.")
