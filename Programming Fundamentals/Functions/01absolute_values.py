# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a list. Use abs().

list_as_string = input().split(" ")
list_as_numbers = []
for number in list_as_string:
    current_num = float(number)
    list_as_numbers.append(current_num)
list_as_numbers = [abs(num) for num in list_as_numbers]
print(list_as_numbers)
