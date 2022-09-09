vegetables_kg_price = float(input())
fruits_kg_price = float(input())
total_kilos_veg = int(input())
total_kilos_fr = int(input())
vegetables_price = vegetables_kg_price * total_kilos_veg
fruits_price = fruits_kg_price * total_kilos_fr
veg_and_fr_price = (vegetables_price + fruits_price) / 1.94
print(f'{veg_and_fr_price:.2f}')
