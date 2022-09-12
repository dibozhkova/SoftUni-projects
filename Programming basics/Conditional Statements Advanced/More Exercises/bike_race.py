num_of_juniors = int(input())
num_of_seniors = int(input())
type_of_trail = input()
price_enter_juniors = 0
price_enter_seniors = 0
if type_of_trail == "trail":
        price_enter_juniors = 5.50
        price_enter_seniors = 7
elif type_of_trail == "cross-country":
    if (num_of_juniors + num_of_seniors) >= 50:
        price_enter_juniors = 8 - (8 * 0.25)
        price_enter_seniors = 9.50 - (9.50 * 0.25)
    else:
        price_enter_juniors = 8
        price_enter_seniors = 9.50
elif type_of_trail == "downhill":
    price_enter_juniors = 12.25
    price_enter_seniors = 13.75
elif type_of_trail == "road":
    price_enter_juniors = 20
    price_enter_seniors = 21.50
all_price_enter = num_of_juniors * price_enter_juniors + num_of_seniors * price_enter_seniors
total_sum = all_price_enter - (all_price_enter * 0.05)
print(f"{total_sum:.2f}")
