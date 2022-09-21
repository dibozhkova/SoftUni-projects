import math

tennis_racket_price = float(input())
tennis_racket_num = int(input())
sneakers = int(input())
sneakers_price = tennis_racket_price * (1 / 6)
rackets_and_sneakers = tennis_racket_num * tennis_racket_price + sneakers * sneakers_price
total_sum = rackets_and_sneakers + rackets_and_sneakers * 0.2
print(f"Price to be paid by Djokovic {math.floor(total_sum * ( 1 / 8))}")
print(f"Price to be paid by sponsors {math.ceil(total_sum * ( 7 / 8))}")
