month = input()
num_overnight = int(input())
price_studio = 0
price_apartment = 0
if month == "May"\
    or month == "October":
    if 7 < num_overnight <= 14:
        price_studio = 50 - (50 * 0.05)
        price_apartment = 65
    elif num_overnight > 14:
        price_studio = 50 - (50 * 0.3)
        price_apartment = 65 - (65 * 0.1)
    else:
        price_studio = 50
        price_apartment = 65
elif month == "June"\
    or month == "September":
    if num_overnight > 14:
        price_studio = 75.2 - (75.2 * 0.2)
        price_apartment = 68.7 - (68.7 * 0.1)
    else:
        price_studio = 75.2
        price_apartment = 68.7
elif month == "July"\
    or month == "August":
    if num_overnight > 14:
        price_apartment = 77 - (77 * 0.1)
        price_studio = 76
    else:
        price_apartment = 77
        price_studio = 76
total_sum_ap = price_apartment * num_overnight
total_sum_st = price_studio * num_overnight
print(f"Apartment: {total_sum_ap:.2f} lv.")
print(f"Studio: {total_sum_st:.2f} lv.")