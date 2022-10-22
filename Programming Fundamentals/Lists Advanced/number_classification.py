# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number


numbers = [int(num) for num in input().split(", ")]
positive_num = (", ".join(str(num) for num in numbers if num >= 0))
negative_num = (", ".join(str(num) for num in numbers if num < 0))
even_num = (", ".join(str(num) for num in numbers if num % 2 == 0))
odd_num = (", ".join(str(num) for num in numbers if num % 2 != 0))
print(f"Positive: {positive_num}")
print(f"Negative: {negative_num}")
print(f"Even: {even_num}")
print(f"Odd: {odd_num}")
