import math

serial = input()
time_serial = int(input())
time_break = int(input())
time_for_lunch = time_break * 0.125
time_for_break = time_break * 0.25
time_break_rest = time_break - (time_for_lunch + time_for_break)
if time_break_rest >= time_serial:
    print(f"You have enough time to watch {serial} and left with {math.ceil(time_break_rest - time_serial)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {math.ceil(time_serial - time_break_rest)} more minutes.")