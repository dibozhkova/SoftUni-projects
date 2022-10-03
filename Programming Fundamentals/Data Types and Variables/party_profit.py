group_size = int(input())
days = int(input())
total_coins = 0
final_group_size = group_size
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        final_group_size -= 2
    if current_day % 15 == 0:
        final_group_size += 5
    total_coins += 50 - 2 * final_group_size
    if current_day % 3 == 0:
        total_coins -= 3 * final_group_size
    if current_day % 5 == 0:
        total_coins += 20 * final_group_size
        if current_day % 3 == 0:
            total_coins -= 2 * final_group_size
coins = int(total_coins / final_group_size)
print(f"{final_group_size} companions received {coins} coins each.")
