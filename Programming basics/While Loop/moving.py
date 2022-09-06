width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
sum_carton = 0
all_free_spaces = width_free_space * length_free_space * height_free_space
input_line = input()
while input_line != "Done":
    carton = int(input_line)
    sum_carton += carton
    if all_free_spaces < sum_carton:
        break
    input_line = input()

diff = abs(all_free_spaces - sum_carton)
if input_line == "Done":
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")
