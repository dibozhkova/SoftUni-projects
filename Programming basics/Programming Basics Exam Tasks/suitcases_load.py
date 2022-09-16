capacity = float(input())

count_suitcase = 0
copy_capacity = capacity

line_input = input()
while line_input != "End":
    volume_suitcase = float(line_input)
    count_suitcase += 1
    if count_suitcase % 3 == 0:
        volume_suitcase = volume_suitcase * 1.1

    # copy_capacity -= volume_suitcase

    if volume_suitcase > copy_capacity:
        count_suitcase -= 1
        print("No more space!")
        break
    copy_capacity -= volume_suitcase
    line_input = input()
if line_input == "End":
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {count_suitcase} suitcases loaded.")
