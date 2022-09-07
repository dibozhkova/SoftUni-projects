num_floors = int(input())
num_rooms = int(input())
floor_letter = ""
for current_floors in range(num_floors, 0, -1):
    for current_rooms in range(num_rooms):
        if current_floors == num_floors:
            floor_letter = "L"
        elif current_floors % 2 == 0:
            floor_letter = "O"
        else:
            floor_letter = "A"
        print(f"{floor_letter}{current_floors}{current_rooms}", end = " ")
    print()
