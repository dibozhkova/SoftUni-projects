budget = float(input())
category = input()
num_of_people = int(input())
transport = 0
ticket_price = 0
if 1 <= num_of_people <= 4:
    transport = budget * 0.75
elif 5 <= num_of_people <= 9:
    transport = budget * 0.6
elif 10 <= num_of_people <= 24:
    transport = budget * 0.5
elif 25 <= num_of_people <= 49:
    transport = budget * 0.4
elif num_of_people >= 50:
    transport = budget * 0.25
if category == "VIP":
        ticket_price = 499.99
elif category == "Normal":
        ticket_price = 249.99
all_sum = ticket_price * num_of_people + transport
if budget >= all_sum:
    print(f"Yes! You have {budget - all_sum:.2f} leva left.")
else:
    print(f"Not enough money! You need {all_sum - budget:.2f} leva.")
