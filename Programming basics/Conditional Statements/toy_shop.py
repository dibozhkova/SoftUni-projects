tip_price = float(input())
puzzles = int(input())
speaking_dolls = int(input())
teddy_bear = int(input())
minions = int(input())
truck = int(input())
all_sum = (puzzles * 2.60) + (speaking_dolls * 3) + (teddy_bear * 4.10) + (minions * 8.20) + (truck * 2)
number_of_toys = puzzles + speaking_dolls + teddy_bear + minions + truck
if number_of_toys >= 50:
    all_sum = all_sum * 0.75
rent = all_sum * 0.1
final_price = all_sum - rent
if final_price >= tip_price:
    print(f"Yes! {(final_price - tip_price):.2f} lv left.")
else:
    print(f"Not enough money! {abs(final_price - tip_price):.2f} lv needed.")
    # решена самостоятелно


