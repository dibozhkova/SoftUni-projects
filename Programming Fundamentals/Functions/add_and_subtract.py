# You will receive three integer numbers. 
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. Print the result of the subtract() function on the console.



def sum_numbers(num1, num2):
    return num1 + num2
def subtract(sum, num3):
    return sum - num3
def add_and_subtract(num1, num2, num3):
    sum_of_integers = sum_numbers(num1, num2)
    result = subtract(sum_of_integers, num3)
    return result

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(add_and_subtract(num_1, num_2, num_3))
