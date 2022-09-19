import sys

easter_bread_num = int(input())
max_chef_grade = -sys.maxsize
win_chef = ""
for bakers in range(1, easter_bread_num + 1):
    total_grade = 0
    baker_name = input()
    grade = input()
    while grade != "Stop":
        grade = int(grade)
        total_grade += grade


        grade = input()
    print(f"{baker_name} has {total_grade} points.")
    if total_grade > max_chef_grade:
        max_chef_grade = total_grade
        win_chef = baker_name
        print(f"{baker_name} is the new number 1!")
    if bakers == easter_bread_num:
        print(f"{win_chef} won competition with {max_chef_grade} points!")
