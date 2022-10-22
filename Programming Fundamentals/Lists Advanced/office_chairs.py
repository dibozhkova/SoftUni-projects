# You are a facility manager at a large business center. One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center. On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors. Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4 visitors). 
# Keep track of the free chairs:
# •	If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".


def check_chairs(numbers_of_rooms):
    total_free_chairs = 0
    needed_chairs = 0
    for numbers_of_rooms in range(1, numbers_of_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {numbers_of_rooms}")
    return total_free_chairs, needed_chairs

numbers_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(numbers_of_rooms)
if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
