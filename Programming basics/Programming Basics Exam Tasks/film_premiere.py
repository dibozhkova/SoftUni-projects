project = input()
film_package = input()
num_tickets = int(input())
price = 0
if film_package == "Drink":
    if project == "John Wick":
        price = 12
    elif project == "Star Wars":
        price = 18
    elif project == "Jumanji":
        price = 9
elif film_package == "Popcorn":
    if project == "John Wick":
        price = 15
    elif project == "Star Wars":
        price = 25
    elif project == "Jumanji":
        price = 11
elif film_package == "Menu":
    if project == "John Wick":
        price = 19
    elif project == "Star Wars":
        price = 30
    elif project == "Jumanji":
        price = 14
if project == "Star Wars" and num_tickets >= 4:
    price *= 0.7
if project == "Jumanji" and num_tickets == 2:
    price *= 0.85

total_sum = num_tickets * price
print(f"Your bill is {total_sum:.2f} leva.")
