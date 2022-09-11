import math

vineyard = int(input())
grapes = float(input())
wine = int(input())
workers = int(input())
grapes_kg = (vineyard * grapes) * 0.4
wine_produced = grapes_kg / 2.5
wine_rest = wine_produced - wine
if wine_produced < wine:
    print(f"It will be a tough winter! More {math.floor(wine - wine_produced)} liters wine needed.")
if wine_produced >= wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine_produced)} liters.")
    print(f"{math.ceil(wine_rest)} liters left -> {math.ceil(wine_rest / workers)} liters per person.")
