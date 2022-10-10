# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one of the following:  "multiply", "divide", "add", "subtract". 


def calculate(operator, number_1, number_2):
    if operator == "multiply":
        return number_1 * number_2
    elif operator == "divide":
        return number_1 // number_2
    elif operator == "add":
        return number_1 + number_2
    elif operator == "subtract":
        return number_1 - number_2

oper = input()
num_1 = int(input())
num_2 = int(input())
print(calculate(oper, num_1, num_2))
