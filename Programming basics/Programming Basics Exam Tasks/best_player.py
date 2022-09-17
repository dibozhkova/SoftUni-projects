import sys

player_name = input()
hack_trick = False
max_goals = - sys.maxsize
best_player = ""
while player_name != "END":
    current_goals = int(input())

    if current_goals > max_goals:
        max_goals = current_goals
        best_player = player_name
        if max_goals >= 10:
            hack_trick = True
            break
        elif max_goals >= 3:
            hack_trick = True
    # last_player = player_name
    player_name = input()
print(f"{best_player} is the best player!")
if hack_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
