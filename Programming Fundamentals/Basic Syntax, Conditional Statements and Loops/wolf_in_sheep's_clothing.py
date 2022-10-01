some_string = input().split(", ")
if some_string[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(some_string)):
        if some_string[i] == "wolf":
            num_of_sheep = len(some_string) - 1 - i
            print(f"Oi! Sheep number {num_of_sheep}! You are about to be eaten by a wolf!")
            break
