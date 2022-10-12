# Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use an appropriate name for the function.


def smallest_number(num_1, num_2, num_3):
    return min(num_1, num_2, num_3)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(smallest_number(number_1, number_2, number_3))
