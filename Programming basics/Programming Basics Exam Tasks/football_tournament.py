football_team_name = input()
number_of_matches_played = int(input())
win_count = 0
equal_count = 0
lose_count = 0
points = 0
for matches in range(1, number_of_matches_played + 1):
    result = input()
    if result == "W":
        win_count += 1
        points += 3
    elif result == "D":
        equal_count += 1
        points += 1
    elif result == "L":
        lose_count += 1
        points = points
if number_of_matches_played > 0:
    print(f"{football_team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {win_count}")
    print(f"## D: {equal_count}" )
    print(f"## L: {lose_count}" )
    percent_win = win_count / number_of_matches_played * 100
    print(f"Win rate: {percent_win:.2f}%")
else:
    print(f"{football_team_name} hasn't played any games during this season.")
