money = float(input())
year_living = int(input())
spent_money = 0
completed_years = 18
for years in range(1800, year_living + 1):

    if years % 2 == 0:
        spent_money = spent_money + 12000

    else:

        spent_money = spent_money + 12000 + (50 * completed_years)
    completed_years = completed_years + 1



if money >= spent_money:
    print(f"Yes! He will live a carefree life and will have {money - spent_money:.2f} dollars left.")
elif money < spent_money:
    diff = abs(money - spent_money)
    print(f"He will need {diff:.2f} dollars to survive.")
