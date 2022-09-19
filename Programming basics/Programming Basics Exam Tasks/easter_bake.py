import math
import sys

easter_bread_num = int(input())

total_sugar = 0
total_flour = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
for every_bread in range(1, easter_bread_num + 1):
    sugar_quantity = int(input())
    flour_quantity = int(input())
    total_sugar += sugar_quantity
    total_flour += flour_quantity
    if max_sugar < sugar_quantity:
        max_sugar = sugar_quantity
    if max_flour < flour_quantity:
        max_flour = flour_quantity
sugar_package = math.ceil(total_sugar / 950)
flour_package = math.ceil(total_flour / 750)
print(f"Sugar: {sugar_package}")
print(f"Flour: {flour_package}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
