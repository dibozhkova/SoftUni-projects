rent_room = float(input())

# •	Торта  – цената ѝ е 20% от наема на залата
# •	Напитки – цената им е 45% по-малко от тази на тортата
# •	Аниматор – цената му е 1/3 от цената за наема на зал

cake_price = rent_room * 0.2
drinks_price = cake_price - cake_price * 0.45
animator = rent_room * (1 / 3)

total_sum = rent_room + cake_price + drinks_price + animator
print(total_sum)
