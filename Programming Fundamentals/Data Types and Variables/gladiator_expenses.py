lost_fights = int(input())
helmed_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmed_broken_count = 0
sword_broken_count = 0
shield_broken_count = 0
armor_broken_count = 0
for current_fight in range(1, lost_fights + 1):
    if current_fight % 2 == 0:
        helmed_broken_count += 1
    if current_fight % 3 == 0:
        sword_broken_count += 1
    if current_fight % 2 == 0 and current_fight % 3 == 0:
        shield_broken_count += 1
        if shield_broken_count % 2 == 0:
            armor_broken_count += 1
expenses = helmed_price * helmed_broken_count + sword_price * sword_broken_count\
           + shield_price * shield_broken_count + armor_price * armor_broken_count
print(f"Gladiator expenses: {expenses:.2f} aureus")
