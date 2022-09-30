line_input = input()
count_coffee = 0
while line_input != "END":
    command = line_input
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        count_coffee += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        count_coffee += 2

    line_input = input()
if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)
