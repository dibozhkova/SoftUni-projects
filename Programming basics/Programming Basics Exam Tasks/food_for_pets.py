days = int(input())
total_food = float(input())
dog_count = 0
cat_count = 0
cookies_count = 0
total_count = 0
for period in range(1, days + 1):
    dog_eaten = int(input())
    cat_eaten = int(input())
    dog_count += dog_eaten
    cat_count += cat_eaten
    total_count = dog_count + cat_count
    if period % 3 == 0:
        cookies_count += (dog_eaten + cat_eaten) * 0.1

print(f"Total eaten biscuits: {round(cookies_count)}gr.")
eaten_food = total_count / total_food * 100
print(f"{eaten_food:.2f}% of the food has been eaten.")
percent_dog = dog_count / total_count * 100
print(f"{percent_dog:.2f}% eaten from the dog.")
percent_cat = cat_count / total_count * 100
print(f"{percent_cat:.2f}% eaten from the cat.")
