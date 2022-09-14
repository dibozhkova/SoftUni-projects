import math

height_wall = int(input())
width_wall = int(input())
percent_without_paint = int(input())
line_input = input()
all_walls = height_wall * width_wall * 4
walls_for_paint = all_walls - all_walls * percent_without_paint / 100
while line_input != "Tired!":
    paint_lt = int(line_input)
    walls_for_paint -= paint_lt
    paint_left = math.ceil(walls_for_paint)
    if paint_left < 0:
        print(f"All walls are painted and you have {abs(paint_left)} l paint left!")
        break
    if walls_for_paint == 0 and paint_left == 0:
        print("All walls are painted! Great job, Pesho!")
        break

    line_input = input()
if line_input == "Tired!":
    print(f"{math.ceil(walls_for_paint)} quadratic m left." )
