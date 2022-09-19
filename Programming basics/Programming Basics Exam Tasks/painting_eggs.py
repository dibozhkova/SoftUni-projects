size_eggs = input()
color_eggs = input()
num_batches = int(input())

if size_eggs == "Large":
    if color_eggs == "Red":
        num_batches *= 16
    elif color_eggs == "Green":
        num_batches *= 12
    elif color_eggs == "Yellow":
        num_batches *= 9
elif size_eggs == "Medium":
    if color_eggs == "Red":
        num_batches *= 13
    elif color_eggs == "Green":
        num_batches *= 9
    elif color_eggs == "Yellow":
        num_batches *= 7
elif size_eggs == "Small":
    if color_eggs == "Red":
        num_batches *= 9
    elif color_eggs == "Green":
        num_batches *= 8
    elif color_eggs == "Yellow":
        num_batches *= 5
total_sum = num_batches * 0.65
print(f"{total_sum:.2f} leva.")
