num_bitcoin = int(input())
num_chinese_yuan = float(input())
commission = float(input())

# •	1 биткойн = 1168 лева.
# •	1 китайски юан = 0.15 долара.
# •	1 долар = 1.76 лева.
# •	1 евро = 1.95 лева.

price_bitcoin_lv = 1168 * num_bitcoin
price_yuan_lv = (0.15 * num_chinese_yuan) * 1.76
total_sum_lv = price_yuan_lv + price_bitcoin_lv
sum_in_euro = total_sum_lv / 1.95
current_commissions = commission / 100
total = sum_in_euro - sum_in_euro * current_commissions
print(f"{total:.2f}")
