# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list of only the even numbers. 


def is_even(number):
    if int(number) % 2 == 0:
        return True

numbers = input().split(" ")
filtered_numbers = []
for current_number in numbers:
    if is_even(current_number):
        filtered_numbers.append(int(current_number))
print(filtered_numbers)
