purchased_food = int(input())

total_eaten_food = 0
purchased_food_in_gr = purchased_food * 1000
line_input = input()
while line_input != "Adopted":
    eaten_food = int(line_input)
    total_eaten_food += eaten_food
    line_input = input()

if total_eaten_food <= purchased_food_in_gr:
    print(f"Food is enough! Leftovers: {purchased_food_in_gr - total_eaten_food} grams." )
else:
    print(f"Food is not enough. You need {abs(total_eaten_food - purchased_food_in_gr)} grams more." )
