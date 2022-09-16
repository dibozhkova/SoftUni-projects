groups = int(input())
all_people = 0
musala_group = 0
monblan_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
for current_group in range(1, groups + 1):
    num_people_in_group = int(input())
    all_people += num_people_in_group
    if num_people_in_group <= 5:
        musala_group += num_people_in_group
    elif 6 <= num_people_in_group <= 12:
        monblan_group += num_people_in_group
    elif 13 <= num_people_in_group <= 25:
        kilimanjaro_group += num_people_in_group
    elif 26 <= num_people_in_group <= 40:
        k2_group += num_people_in_group
    elif num_people_in_group >= 41:
        everest_group += num_people_in_group
print(f"{musala_group / all_people * 100:.2f}%")
print(f"{monblan_group / all_people * 100:.2f}%")
print(f"{kilimanjaro_group / all_people * 100:.2f}%")
print(f"{k2_group / all_people * 100:.2f}%")
print(f"{everest_group / all_people * 100:.2f}%")
