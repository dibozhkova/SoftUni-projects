num_group = int(input())
group_musala = 0
group_montblanc = 0
group_kilimanjaro = 0
group_k2 = 0
group_everest = 0

for i in range(1, num_group + 1):
    people = int(input())
    if people <= 5:
        group_musala = group_musala + people
    elif 6 <= people <= 12:
        group_montblanc = group_montblanc + people
    elif 13 <= people <= 25:
        group_kilimanjaro = group_kilimanjaro + people
    elif 26 <= people <= 40:
        group_k2 = group_k2 + people
    elif people >= 41:
        group_everest = group_everest + people

all_people = group_musala + group_montblanc + group_kilimanjaro + group_k2 + group_everest


percent_musala = (group_musala / all_people) * 100
print(f"{percent_musala:.2f}%")
percent_montblanc = (group_montblanc / all_people) * 100
print(f"{percent_montblanc:.2f}%")
percent_kilimanjaro = (group_kilimanjaro / all_people) * 100
print(f"{percent_kilimanjaro:.2f}%")
percent_k2 = (group_k2 / all_people) * 100
print(f"{percent_k2:.2f}%")
percent_everest = (group_everest / all_people) * 100
print(f"{percent_everest:.2f}%")
