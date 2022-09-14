import sys

line_input = input()
max_score = -sys.maxsize
winner_name = ""
while line_input != "Stop":
    player_name = line_input
    score = 0
    for letter in player_name:
        number = int(input())
        if number == ord(letter):
            score += 10
        else:
            score += 2
        if score >= max_score:
            max_score = score
            winner_name = player_name

    line_input = input()
print(f"The winner is {winner_name} with {max_score} points!")
