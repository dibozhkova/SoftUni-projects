desire_profit = float(input())
line_input = input()
total_sum = 0
while line_input != "Party!":
    cocktail = line_input
    num_cocktails = int(input())
    price_cocktails = len(cocktail) * num_cocktails
    if price_cocktails % 2 == 0:
        price_cocktails = price_cocktails
    else:
        price_cocktails *= 0.75
    total_sum += price_cocktails
    if total_sum >= desire_profit:
        print(f"Target acquired.")
        break

    line_input = input()
if line_input == "Party!":
    diff = abs(desire_profit - total_sum)
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {total_sum:.2f} leva.")
