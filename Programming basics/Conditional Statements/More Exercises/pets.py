import math

days = int(input())
food_left = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_g = float(input())
dog = days * dog_food_kg
cat = days * cat_food_kg
turtle = days * (turtle_food_g / 1000)
all_food = dog + cat + turtle
if food_left >= all_food:
    print(f"{math.floor(food_left - all_food)} kilos of food left.")
else:
    print(f"{math.ceil(all_food - food_left)} more kilos of food are needed.")
