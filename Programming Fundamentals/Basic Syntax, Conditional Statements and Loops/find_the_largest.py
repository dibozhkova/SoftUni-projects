number = int(input())
number_as_string = str(number)
list_of_number = []
for digit in number_as_string:
    list_of_number.append(digit)
list_of_number.sort(reverse = True)
print("".join(list_of_number))
