num_guest = int(input())
price_person = float(input())
budget = float(input())

# •	Между 10 (вкл.) и 15 (вкл.) човека -> 15 % отстъпка от куверта за един човек
# •	Между 15 и 20 (вкл.) човека -> 20 % отстъпка от куверта за един човек
# •	Над 20 човека -> 25 % отстъпка от куверта за един човек
if 10 <= num_guest <= 15:
    price_person *= 0.85
elif 15 < num_guest <= 20:
    price_person *= 0.8
elif num_guest > 20:
    price_person *= 0.75

price_cake = budget * 0.1
all_sum = num_guest * price_person + price_cake
diff = abs(all_sum - budget)
if budget >= all_sum:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
