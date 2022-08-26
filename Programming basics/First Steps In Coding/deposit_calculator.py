amount_deposited = float(input())
term = int(input())
annual_rate = float(input())
annual_year = amount_deposited * annual_rate / 100
annual_month = annual_year / 12
total_sum = amount_deposited + term * annual_month
print(total_sum)
