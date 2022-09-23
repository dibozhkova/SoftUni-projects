number = int(input())
counter_2 = 0
counter_3 = 0
counter_4 = 0
for numbers in range(number):
    current_number = int(input())
    if current_number % 2 == 0:
        counter_2 += 1
    if current_number % 3 == 0:
        counter_3 += 1
    if current_number % 4 == 0:
        counter_4 += 1
percent_num_counter_2 = (counter_2 / number) * 100
percent_num_counter_3 = (counter_3 / number) * 100
percent_num_counter_4 = (counter_4 / number) * 100
print(f"{percent_num_counter_2:.2f}%")
print(f"{percent_num_counter_3:.2f}%")
print(f"{percent_num_counter_4:.2f}%")
