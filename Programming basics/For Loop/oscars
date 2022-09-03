actor_name = input()
points_from_academy = float(input())
raters = int(input())

total_points = points_from_academy
for points in range(1, raters + 1):

    name_rater = input()
    points_rater = float(input())


    current_points = (len(name_rater) * points_rater) / 2
    total_points = total_points + current_points

    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
