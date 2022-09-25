num_people = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
for people in range(num_people):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1
training_people_count = back + chest + legs + abs
product_count = protein_bar + protein_shake
percent_training_people = training_people_count / num_people * 100
percent_bought_product = product_count / num_people * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percent_training_people:.2f}% - work out")
print(f"{percent_bought_product:.2f}% - protein")
