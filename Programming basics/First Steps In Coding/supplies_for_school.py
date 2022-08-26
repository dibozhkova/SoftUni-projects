pens_package = int(input())
markers_package = int(input())
preparation_lt = int(input())
reduction = int(input())
pens_price = pens_package * 5.80
markers_price = markers_package * 7.20
preparation_price = preparation_lt * 1.20
all_materials = pens_price + markers_price + preparation_price
reduction_price = all_materials - (all_materials * reduction / 100)
print(f"Ani will need {reduction_price} lv.")
