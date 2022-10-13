# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"


def min_max_sum(num):
    min_number = 0
    max_number = 0
    total_sum = 0
    for number in num:
        min_number = min(num)
        max_number = max(num)
        total_sum += number
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {total_sum}")

numbers = [int(s) for s in input().split(" ")]
min_max_sum(numbers)
