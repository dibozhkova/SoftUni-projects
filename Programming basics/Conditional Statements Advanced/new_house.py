type_of_flower = input()
num_of_flower = int(input())
budget = int(input())
price_for_one_flower = 0
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
if type_of_flower == "Roses":
    if num_of_flower > 80:
        price_for_one_flower = 5 - (5 * 0.1)
    else:
        price_for_one_flower = 5
elif type_of_flower == "Dahlias":
    if num_of_flower > 90:
        price_for_one_flower = 3.80 - (3.80 * 0.15)
    else:
        price_for_one_flower = 3.80
elif type_of_flower == "Tulips":
    if num_of_flower > 80:
        price_for_one_flower = 2.80 - (2.80 * 0.15)
    else:
        price_for_one_flower = 2.80
elif type_of_flower == "Narcissus":
    if num_of_flower < 120:
        price_for_one_flower = 3 + (3 * 0.15)
    else:
        price_for_one_flower = 3
elif type_of_flower == "Gladiolus":
    if num_of_flower < 80:
        price_for_one_flower = 2.50 + (2.50 * 0.20)
    else:
        price_for_one_flower = 2.50
price_all_flowers = num_of_flower * price_for_one_flower

if budget >= price_all_flowers:
    print(f"Hey, you have a great garden with {num_of_flower} {type_of_flower} and {budget - price_all_flowers:.2f} leva left.")
else:
    print(f"Not enough money, you need {price_all_flowers - budget:.2f} leva more.")

