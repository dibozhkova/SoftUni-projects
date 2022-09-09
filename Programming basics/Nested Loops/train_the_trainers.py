num_jury = int(input())

line_input = input()
sum_all_grades = 0
count_grades = 0
while line_input != "Finish":
    presentation = line_input

    sum_current_grade = 0
    for i in range(1, num_jury + 1):
        current_grade = float(input())
        sum_all_grades += current_grade
        count_grades += 1
        sum_current_grade += current_grade
    avr_grade_current = sum_current_grade / num_jury
    print(f"{presentation} - {avr_grade_current:.2f}.")
    line_input = input()

final_avr = sum_all_grades / count_grades
print(f"Student's final assessment is {final_avr:.2f}.")
