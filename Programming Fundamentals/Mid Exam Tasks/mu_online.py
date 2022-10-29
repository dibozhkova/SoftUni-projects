rooms = input().split("|")
coins = 0
health = 100
best_room = 0
is_dead = False
for room in rooms:
    best_room += 1
    current_room = room.split()
    command = current_room[0]
    if command == "potion":
        health_points = int(current_room[1])
        if health + health_points > 100:
            health_points = 100 - health
            health = 100
        else:
            health += health_points
        print(f'You healed for {health_points} hp.')
        print(f'Current health: {health} hp.')
    elif command == "chest":
        coins_found = int(current_room[1])
        print(f"You found {coins_found} bitcoins.")
        coins += coins_found
    else:
        monster = current_room[0]
        attack = int(current_room[1])
        health -= attack
        if health > 0:
            print(f'You slayed {monster}.')
        else:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {best_room}')
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")
    
    
    
    
# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
# o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# o	First print: "You healed for {amount} hp."
# o	After that, print your current health: "Current health: {health} hp."
# •	"chest"
# o	You've found some bitcoins, the number in the second part.
# o	Print: "You found {amount} bitcoins."
# •	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster. 
# You should remove the monster's attack from your health. 
# o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
# o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach: "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines: 
# "You've made it!"
# "Bitcoins: {bitcoins}"
# "Health: {health}"
# Input / Constraints
# You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
# Output
# Print the corresponding messages described above.
