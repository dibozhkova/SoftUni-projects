num_preparation = int(input())
input_line = input()
total_preparation = num_preparation * 750
count = 0
dishes_num = 0
pots_num = 0
while input_line != "End":
    dishes = int(input_line)
    count += 1
    if count % 3 == 0:
        pots_num += dishes
        total_preparation = total_preparation - dishes * 15
    else:
        dishes_num += dishes
        total_preparation = total_preparation - dishes * 5
    if total_preparation < 0:
        break
    input_line = input()

if total_preparation >= 0:
    print("Detergent was enough!")
    print(f"{dishes_num} dishes and {pots_num} pots were washed.")
    print(f"Leftover detergent {total_preparation} ml.")
else:
    print(f"Not enough detergent, {abs(total_preparation)} ml. more necessary!")
