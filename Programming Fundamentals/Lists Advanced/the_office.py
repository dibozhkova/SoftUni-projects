# You will receive two lines of input: 
# •	a list of employees' happiness as a string of numbers separated by a single space 
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office. 
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"


employees_happiness = [int(el) for el in input().split()]
factor = int(input())
multiply_factor = [el * factor for el in employees_happiness]
avr_happiness = sum(multiply_factor) / len(employees_happiness)
after_filtration = [el for el in multiply_factor if el >= avr_happiness]
if len(employees_happiness) / 2 <= len(after_filtration):
    print(f"Score: {len(after_filtration)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(after_filtration)}/{len(employees_happiness)}. Employees are not happy!")
