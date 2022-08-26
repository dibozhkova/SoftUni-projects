year_tax = int(input())
shoes_price = year_tax * 0.60
suit_price = shoes_price * 0.80
ball_price = suit_price / 4
acc = ball_price / 5
total_sum = shoes_price + suit_price + ball_price + acc + year_tax
print(total_sum)