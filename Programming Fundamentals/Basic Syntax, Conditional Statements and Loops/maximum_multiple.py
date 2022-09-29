import sys

divisor = int(input())
boundary = int(input())
largest_divisible = -sys.maxsize
for number in range(divisor, boundary + 1):
    if number % divisor == 0 and number > largest_divisible:
        largest_divisible = number
print(f"{largest_divisible}")
