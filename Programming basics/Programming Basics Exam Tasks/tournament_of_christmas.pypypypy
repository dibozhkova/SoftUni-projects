days_of_tour = int(input())

total_money = 0
total_win_count = 0
total_lose_count = 0
for day in range(1, days_of_tour + 1):
    money = 0
    win_count = 0
    lose_count = 0
    line_input = input()
    while line_input != "Finish":
        sport = line_input
        result = input()
        if result == "win":
            money += 20
            win_count += 1
            total_win_count += 1
        elif result == "lose":
            money = money
            lose_count += 1
            total_lose_count += 1

        line_input = input()
    if win_count > lose_count:
        money = money * 1.1
        total_money += money
    else:
        total_money += money

if total_win_count > total_lose_count:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
