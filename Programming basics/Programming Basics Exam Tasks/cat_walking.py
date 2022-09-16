walk_in_minutes = int(input())
num_of_walking = int(input())
consumed_calories = int(input())

total_walking = walk_in_minutes * num_of_walking
burn_calories = total_walking * 5
half_consume_calories = consumed_calories / 2
if burn_calories >= half_consume_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")
