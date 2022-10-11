# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().


list_as_string = input().split(" ")
list_as_rounded_number = []
for num in list_as_string:
    current_num = round(float(num))
    list_as_rounded_number.append(current_num)
print(list_as_rounded_number)
