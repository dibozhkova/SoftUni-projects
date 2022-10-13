# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a sorted list of numbers in ascending order.


def num_sort(numbers):
    sorted_numbers = []
    for current_number in numbers:
        sorted_numbers.append(int(current_number))
    return sorted(sorted_numbers)

number = input().split(" ")
print(num_sort(number))
