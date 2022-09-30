budjet = float(input())
flour_kg_price = float(input())
eggs_price = flour_kg_price * 0.75
milk_lt_price = flour_kg_price + flour_kg_price * 0.25
milk_for_one_bread_price = milk_lt_price / 4
one_bread_price = eggs_price + flour_kg_price + milk_for_one_bread_price
count_loaves = 0
colored_eggs = 0
copy_budget = budjet
while copy_budget > one_bread_price:
    count_loaves += 1
    colored_eggs += 3
    copy_budget -= one_bread_price
    if count_loaves % 3 == 0:
        colored_eggs -= count_loaves - 2
print(f"You made {count_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {copy_budget:.2f}BGN left.")
