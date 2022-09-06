change = float(input())
change_coins = round(change * 100)
count_change = 0

while change_coins > 0:
    if change_coins >= 200:
        count_change += 1
        change_coins -= 200
    elif change_coins >= 100:
        count_change += 1
        change_coins -= 100
    elif change_coins >= 50:
        count_change += 1
        change_coins -= 50
    elif change_coins >= 20:
        count_change += 1
        change_coins -= 20
    elif change_coins >= 10:
        count_change += 1
        change_coins -= 10
    elif change_coins >= 5:
        count_change += 1
        change_coins -= 5
    elif change_coins >= 2:
        count_change += 1
        change_coins -= 2
    elif change_coins >= 1:
        count_change += 1
        change_coins -= 1

print(count_change)
