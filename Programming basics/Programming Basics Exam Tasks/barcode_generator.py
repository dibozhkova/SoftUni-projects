start_number = int(input())
end_number = int(input())

first_num_start = start_number // 1000
second_num_start = start_number // 100 % 10
third_num_start = start_number // 10 % 10
four_num_start = start_number % 10

first_num_end = end_number // 1000
second_num_end = end_number // 100 % 10
third_num_end = end_number // 10 % 10
four_num_end = end_number % 10

for num_1 in range(first_num_start, first_num_end + 1):
    for num_2 in range(second_num_start, second_num_end + 1):
        for num_3 in range(third_num_start, third_num_end + 1):
            for num_4 in range(four_num_start, four_num_end + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end = " ")
