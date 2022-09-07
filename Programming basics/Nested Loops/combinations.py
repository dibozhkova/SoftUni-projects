number = int(input())
count_valid_combination = 0
for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            result = x1 + x2 + x3
            if result == number:
                count_valid_combination += 1
print(count_valid_combination)
