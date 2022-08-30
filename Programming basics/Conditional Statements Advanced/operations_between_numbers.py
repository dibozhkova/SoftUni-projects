number_1 = int(input())
number_2 = int(input())
operator = input()
result = 0
even_or_odd = ""
if operator == "+":
    result = number_1 + number_2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number_1} {operator} {number_2} = {result} - {even_or_odd}")
elif operator == "-":
    result = number_1 - number_2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number_1} {operator} {number_2} = {result} - {even_or_odd}")

elif operator == "*":
    result = number_1 * number_2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number_1} {operator} {number_2} = {result} - {even_or_odd}")

if number_2 == 0:
    if operator == "/" or operator == "%":
        print(f"Cannot divide {number_1} by zero")
elif number_2 != 0:
    if operator == "/":
        print(f"{number_1} / {number_2} = {number_1 / number_2:.2f}")
    elif operator == "%":
        print(f"{number_1} % {number_2} = {number_1 % number_2}")

