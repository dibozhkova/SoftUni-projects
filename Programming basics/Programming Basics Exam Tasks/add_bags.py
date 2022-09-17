price_baggage_under_20kg = float(input())
kg_of_baggage = float(input())
days_until_trip = int(input())
num_baggage = int(input())
tax_baggage = 0
# Таксите за багаж се изчисляват въз основа на теглото на чекирания багаж:
# •	до 10кг – 20% от цената на багаж над 20кг
# •	между 10кг и 20кг вкл. – 50% от цената на багаж над 20кг.
# •	над 20кг – таксата се чете от конзолата
if kg_of_baggage < 10:
    tax_baggage = price_baggage_under_20kg * 0.2
elif 10 <= kg_of_baggage <= 20:
    tax_baggage = price_baggage_under_20kg / 2
else:
    tax_baggage = price_baggage_under_20kg

if days_until_trip > 30:
    tax_baggage += tax_baggage * 0.1
elif 7 <= days_until_trip <= 30:
    tax_baggage += tax_baggage * 0.15
elif days_until_trip < 7:
    tax_baggage += tax_baggage * 0.4
price_baggage = tax_baggage * num_baggage
print(f"The total price of bags is: {price_baggage:.2f} lv.")
