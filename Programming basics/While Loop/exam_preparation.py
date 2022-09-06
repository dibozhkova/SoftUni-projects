poor_grades = int(input())

sum_grades = 0
count_task = 0
fail_count = 0
last_task = ""
task_name = input()
while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        fail_count += 1
        if fail_count == poor_grades:
            break

    sum_grades += grade
    count_task += 1
    last_task = task_name

    task_name = input()
if fail_count < poor_grades:
    print(f"Average score: {sum_grades / count_task:.2f}")
    print(f"Number of problems: {count_task}")
    print(f"Last problem: {last_task}")
else:
    print(f"You need a break, {fail_count} poor grades.")
