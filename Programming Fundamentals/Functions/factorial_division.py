# Write a function that receives two integer numbers. Calculate the factorial of each number. 
# Divide the first result by the second and print the division formatted to the second decimal point.


def factorial_division(num1, num2):
    factorial_num1 = 1
    factorial_num2 = 1
    for digit in range(1, num1 + 1):
        factorial_num1 *= digit
    for digit in range(1, num2 + 1):
        factorial_num2 *= digit
    division = factorial_num1 / factorial_num2
    print(f"{division:.2f}")

first_number = int(input())
second_number = int(input())
factorial_division(first_number, second_number)
