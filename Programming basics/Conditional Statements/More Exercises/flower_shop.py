import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())
bouquet = (magnolias * 3.25) + (hyacinths * 4) + (roses * 3.5) + (cacti * 8)
tax = bouquet * 0.05
total_sum = bouquet - tax
if total_sum >= gift_price:
    print(f"She is left with {math.floor(total_sum - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - total_sum)} leva.")
