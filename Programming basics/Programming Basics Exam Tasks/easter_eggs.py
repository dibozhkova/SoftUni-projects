import sys

num_painted_eggs = int(input())

red_count = 0
orange_count = 0
blue_count = 0
green_count = 0
max_count = -sys.maxsize
color = ""
for eggs in range(1, num_painted_eggs + 1):
    color_eggs = input()
    if color_eggs == "red":
        red_count += 1
    elif color_eggs == "orange":
        orange_count += 1
    elif color_eggs == "blue":
        blue_count += 1
    elif color_eggs == "green":
        green_count += 1

if red_count > max_count:
    max_count = red_count
    color = "red"
if orange_count > max_count:
    max_count = orange_count
    color = "orange"
if blue_count > max_count:
    max_count = blue_count
    color = "blue"
if green_count > max_count:
    max_count = green_count
    color = "green"
print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_count} -> {color}")
