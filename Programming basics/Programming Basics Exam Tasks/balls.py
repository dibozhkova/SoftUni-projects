import math

number = int(input())

points = 0
red_balls_count = 0
orange_balls_count = 0
yellow_balls_count = 0
white_balls_count = 0
black_balls_count = 0
other_balls_count = 0

for balls in range(1, number + 1):
    current_color = input()
    if current_color == "red":
        points += 5
        red_balls_count += 1
    elif current_color == "orange":
        points += 10
        orange_balls_count += 1
    elif current_color == "yellow":
        points += 15
        yellow_balls_count += 1
    elif current_color == "white":
        points += 20
        white_balls_count += 1
    elif current_color == "black":
        points = math.floor(points / 2)
        black_balls_count += 1
    else:
        other_balls_count += 1
        points = points
print(f"Total points: {points}")
print(f"Red balls: {red_balls_count}")
print(f"Orange balls: {orange_balls_count}")
print(f"Yellow balls: {yellow_balls_count}")
print(f"White balls: {white_balls_count}")
print(f"Other colors picked: {other_balls_count}")
print(f"Divides from black balls: {black_balls_count}")
