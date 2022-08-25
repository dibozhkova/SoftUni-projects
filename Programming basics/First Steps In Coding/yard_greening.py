square_meters_for_greening = float(input())
price_for_one_square_meter = 7.61
discount_for_total_price = 0.18
total_price = square_meters_for_greening * price_for_one_square_meter
print(f"The final price is: {total_price - total_price * discount_for_total_price} lv.")
print(f"The discount is {total_price * discount_for_total_price} lv.")