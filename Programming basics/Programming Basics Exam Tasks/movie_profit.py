movie = input()
days = int(input())
tickets = int(input())
price_ticket = float(input())
percent_cinema = int(input())
num_total_tickets = days * tickets
total_price_tickets = num_total_tickets * price_ticket
total_price = total_price_tickets - total_price_tickets * percent_cinema / 100
print(f"The profit from the movie {movie} is {total_price:.2f} lv.")
