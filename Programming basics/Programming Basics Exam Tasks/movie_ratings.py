import sys

num_films = int(input())
max_rating_film = -sys.maxsize
min_rating_film = sys.maxsize
name_max = ""
name_min = ""
total_rating = 0
for films in range(1, num_films + 1):
    name_film = input()
    rating_film = input()
    total_rating += float(rating_film)
    if float(rating_film) > max_rating_film:
        max_rating_film = float(rating_film)
        name_max = name_film
    elif float(rating_film) < min_rating_film:
        min_rating_film = float(rating_film)
        name_min = name_film
print(f"{name_max} is with highest rating: {max_rating_film:.1f}")
print(f"{name_min} is with lowest rating: {min_rating_film:.1f}")
avr_rating = total_rating / num_films
print(f"Average rating: {avr_rating:.1f}")
