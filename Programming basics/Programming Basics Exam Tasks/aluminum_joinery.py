num_windows = int(input())
type_of_windows = input()
shipment_method = input()
price_window = 0
total_sum = 0
order_is_valid = True
if type_of_windows == "90X130":
    price_window = 110

    if num_windows > 60:
        price_window = price_window - price_window * 0.08
    elif num_windows > 30:
        price_window -= price_window * 0.05
    else:
        price_window = price_window
elif type_of_windows == "100X150":
    price_window = 140

    if num_windows > 80:
        price_window -= price_window * 0.1
    elif num_windows > 40:
        price_window -= price_window * 0.06
elif type_of_windows == "130X180":
    price_window = 190

    if num_windows > 50:
        price_window -= price_window * 0.12
    elif num_windows > 20:
        price_window -= price_window * 0.07
elif type_of_windows == "200X300":
    price_window = 250

    if num_windows > 50:
        price_window -= price_window * 0.14
    elif num_windows > 25:
        price_window -= price_window * 0.09
total_sum = price_window * num_windows

if shipment_method == "With delivery":
    total_sum += 60
else:
    total_sum = total_sum

if num_windows > 99:
    total_sum = total_sum * 0.96
elif num_windows < 10:
    order_is_valid = False

if not order_is_valid:
    print("Invalid order")
else:
    print(f"{total_sum:.2f} BGN")
