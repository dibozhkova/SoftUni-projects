list_of_numbers_as_str = input().split()
count_of_numbers_to_remove = int(input())
list_of_numbers_as_digits = []
for element in list_of_numbers_as_str:
    list_of_numbers_as_digits.append(int(element))
while count_of_numbers_to_remove > 0:
    list_of_numbers_as_digits.remove(min(list_of_numbers_as_digits))
    count_of_numbers_to_remove -= 1
print(*list_of_numbers_as_digits, sep = ", ")
