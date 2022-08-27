from math import pi
type_of_figure = input()
area = 0
if type_of_figure == "square":
    side = float(input())
    area = side * side
elif type_of_figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
elif type_of_figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
elif type_of_figure == "triangle":
    side = float(input())
    hight = float(input())
    area = side * hight / 2
print(f"{area:.3f}")