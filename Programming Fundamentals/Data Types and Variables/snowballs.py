num_snowball = int(input())
highest_value = 0
weight = 0
time = 0
quality = 0
for current_snowball in range(num_snowball):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > highest_value:
        highest_value = snowball_value
        weight = snowball_weight
        time = snowball_time
        quality = snowball_quality
print(f"{weight} : {time} = {int(highest_value)} ({quality})")
