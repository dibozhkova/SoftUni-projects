number = int(input())
for num in range(1, number +1):
    sum_of_digit = 0
    digit = num
    while digit > 0:
        sum_of_digit += digit % 10
        digit //= 10
    if sum_of_digit == 5 or sum_of_digit == 7 or sum_of_digit == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
