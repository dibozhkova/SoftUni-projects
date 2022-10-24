needed_experience = float(input())
count_of_battles = int(input())
collected_exp = 0
is_collect = False
for current_battle in range(1, count_of_battles + 1):
    earned_exp = float(input())
    if current_battle % 3 == 0:
        earned_exp += earned_exp * 0.15
    if current_battle % 5 == 0:
        earned_exp -= earned_exp * 0.10
    if current_battle % 15 == 0:
        earned_exp += earned_exp * 0.05
    collected_exp += earned_exp
    if collected_exp >= needed_experience:
        is_collect = True
        print(f"Player successfully collected his needed experience for {current_battle} battles.")
        break
if not is_collect:
    print(f"Player was not able to collect the needed experience, {needed_experience - collected_exp:.2f} more needed.")
