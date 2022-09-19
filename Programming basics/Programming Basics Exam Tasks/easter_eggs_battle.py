first_player_eggs = int(input())
second_player_eggs = int(input())
line_input = input()
while line_input != "End":
    winner = line_input
    if winner == "one":
        second_player_eggs -= 1
    elif winner == "two":
        first_player_eggs -= 1
    if first_player_eggs == 0:
        break
    elif second_player_eggs == 0:
        break


    line_input = input()

if line_input == "End":
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
if first_player_eggs == 0:
    print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
elif second_player_eggs == 0:
    print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
