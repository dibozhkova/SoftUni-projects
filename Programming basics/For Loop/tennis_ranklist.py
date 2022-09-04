import math

num_turnir = int(input())
start_points = int(input())

w = 0
f = 0
sf = 0
num_won = 0
for i in range(1, num_turnir + 1):
    stage = (input())
    if stage == "W":
        w = w + 2000
        num_won = num_won + 1
    elif stage == "F":
        f = f + 1200
    elif stage == "SF":
        sf = sf + 720

total_points = w + f + sf + start_points
average_points = math.floor((w + f + sf) / num_turnir)
percent_won = (num_won / num_turnir) * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")
