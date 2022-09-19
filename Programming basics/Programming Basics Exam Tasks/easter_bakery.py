flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
num_eggs = int(input())
num_yeast = int(input())

# •	цената на килограм захар е с 25% по-ниска от тази на килограм брашно
# •	цената на една кора с яйца е с 10% по-висока от цената на килограм брашно
# •	цената на един пакет мая е с 80% по-ниска от цената на килограм захар


sum_sugar = flour_price * 0.75
sum_eggs = flour_price * 1.1
sum_yeast = sum_sugar * 0.2
total_sum = flour_kg * flour_price + sugar_kg * sum_sugar + num_eggs * sum_eggs + num_yeast * sum_yeast
print(f"{total_sum:.2f}")
