actor_name = input()
point_from_academy = float(input())
number_of_assessors = int(input())
for assessors in range(number_of_assessors):
    name_assessors = input()
    points_from_assessors = float(input())
    point_from_academy += (len(name_assessors) * points_from_assessors) / 2
    if point_from_academy >= 1250.5:
        break
if point_from_academy >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {point_from_academy:.1f}!")
else:
    diff = 1250.5 - point_from_academy
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
