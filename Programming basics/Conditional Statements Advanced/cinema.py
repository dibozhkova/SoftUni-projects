type_of_projection = input()
number_row = int(input())
number_column = int(input())
ticket_price = 0
full_movie_theater = number_row * number_column
if type_of_projection == "Premiere":
    ticket_price = 12
elif type_of_projection == "Normal":
    ticket_price = 7.50
elif type_of_projection == "Discount":
    ticket_price = 5
total_sum = full_movie_theater * ticket_price
print(f"{total_sum:.2f} leva")
