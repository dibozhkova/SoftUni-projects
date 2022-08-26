nylon = int(input())
paint = int(input())
thinner = int(input())
workers_hours = int(input())
nylon_quantity = (nylon + 2) * 1.50
pain_quantity = (paint * 14.50) * 0.1 + (paint * 14.50)
thinner_quantity = thinner * 5.00
bags = 0.40
all_materials = nylon_quantity + pain_quantity + thinner_quantity + bags
workers_per_hour = all_materials * workers_hours * 0.3
sum_of_all_expenses = all_materials + workers_per_hour
print(f"Sum of all expenses is {sum_of_all_expenses} lv.")
