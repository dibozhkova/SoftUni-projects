chiken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())
chiken_menu_price = chiken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegan_menu_price = vegan_menu * 8.15
all_menu_price = chiken_menu_price + fish_menu_price + vegan_menu_price
delivery = 2.50
desert = (chiken_menu_price + fish_menu_price + vegan_menu_price) * 0.2
all_sum = all_menu_price + delivery + desert
print(f"The price of the order is {all_sum} lv.")
