import sys

number_n = int(input())
sum_numbers = 0
max_num = -sys.maxsize
for numbers in range(number_n):
    current_num = int(input())
    sum_numbers = sum_numbers + current_num
    if current_num > max_num:
        max_num = current_num
others_num_sum = sum_numbers - max_num
if others_num_sum == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    diff = abs(others_num_sum - max_num)
    print(f"Diff = {diff}")
