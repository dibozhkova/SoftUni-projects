strawberries_price = float(input())
bananas_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())
# •	цената на малините е на половина по-ниска от тази на ягодите;
# •	цената на портокалите е с 40% по-ниска от цената на малините;
# •	цената на бананите е с 80% по-ниска от цената на малините.
raspberries_price = strawberries_price / 2
orange_price = raspberries_price - raspberries_price * 0.4
bananas_price = raspberries_price - raspberries_price * 0.8
all_sum = strawberries_kg * strawberries_price + raspberries_kg * raspberries_price + orange_kg * orange_price + bananas_kg * bananas_price
print(f"{all_sum:.2f}")
