# You will receive three integer numbers. Write a program that finds if their multiplication (the result) is negative, positive, or zero. 
# Try to do this WITHOUT multiplying the 3 numbers.


def multiplication(num1, num2, num3):
    list_of_num = [num1, num2, num3]
    if 0 in list_of_num:
        return "zero"
    counter_negative_num = 0
    for digit in list_of_num:
        if digit < 0:
            counter_negative_num += 1
    if counter_negative_num == 1 or counter_negative_num == 3:
        return "negative"
    return "positive"


number1 = int(input())
number2 = int(input())
number3 = int(input())
print(multiplication(number1, number2, number3))
