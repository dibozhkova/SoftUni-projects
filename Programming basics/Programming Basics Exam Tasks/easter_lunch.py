num_easter_bread = int(input())
num_eggs = int(input())
cookies = int(input())

# •	Козунак  – 3.20 лв.
# •	Яйца –  4.35 лв. за кора с 12 яйца
# •	Курабии – 5.40 лв. за килограм
# •	Боя за яйца - 0.15 лв. за яйце

easter_bread_price = num_easter_bread * 3.2
eggs_price = num_eggs * 4.35
cookies_price = cookies * 5.4
paint_egs = num_eggs * 12 * 0.15
total_sum = easter_bread_price + eggs_price + cookies_price + paint_egs
print(f"{total_sum:.2f}")
