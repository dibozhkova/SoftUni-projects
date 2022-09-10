x_height_house = float(input())
y_length_side_wall = float(input())
h_height_triangle_roof = float(input())
front_wall = (x_height_house * x_height_house) - (1.2 * 2)
back_wall = x_height_house * x_height_house
side_wall1 = (x_height_house * y_length_side_wall) - (1.5 * 1.5)
side_wall2 = (x_height_house * y_length_side_wall) - (1.5 * 1.5)
all_wall_area = front_wall + back_wall + side_wall1 + side_wall2
# print(all_wall_area) вярно
roolf_area = 2 * (x_height_house * y_length_side_wall) + 2 * (x_height_house * h_height_triangle_roof / 2)
# print(roolf_area) вярно
green_paint_lt = all_wall_area / 3.4
red_paint_lt = roolf_area / 4.3
print(f'{green_paint_lt:.2f}')
print(f'{red_paint_lt:.2f}')
