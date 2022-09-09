number = int(input())

for num in range(1111, 9999 + 1):
    current_num = str(num)
    count_digit = 0
    for index, digit in enumerate(current_num):
        if int(digit) == 0:
            count_digit = count_digit
            continue
        if number % int(digit) == 0:
            count_digit += 1


        if count_digit == 4:
            print(current_num, end = " ")
