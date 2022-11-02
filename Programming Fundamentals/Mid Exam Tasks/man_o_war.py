pirate_ship = [int(i) for i in input().split(">")]
warship = [int(i) for i in input().split(">")]
max_health = int(input())
line_input = input().split()
game_over = False
while line_input[0] != "Retire":
    command = line_input[0]
    if command == "Fire":
        index = int(line_input[1])
        damage = int(line_input[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                game_over = True
                print("You won! The enemy ship has sunken.")
                break
    elif command == "Defend":
        start_index = int(line_input[1])
        end_index = int(line_input[2])
        damage = int(line_input[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for section in range(start_index, end_index + 1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    game_over = True
                    print("You lost! The pirate ship has sunken.")
                    break
    elif command == "Repair":
        index = int(line_input[1])
        health = int(line_input[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    elif command == "Status":
        counter = 0
        for section in pirate_ship:
            if section < max_health * 0.2:
                counter += 1
        print(f"{counter} sections need repair.")


    line_input = input().split()
if not game_over:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")
    
    
    
#     The pirates encounter a huge Man-O-War at sea. 
# Create a program that tracks the battle and either chooses a winner or prints a stalemate. 
# On the first line, you will receive the status of the pirate ship, which is a string representing integer sections separated by ">". 
# On the second line, you will receive the same type of status, but for the warship: 
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach. 
# The following lines represent commands until "Retire":
# •	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and if not, skip the command. 
# If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."
# •	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). 
# Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
# "You lost! The pirate ship has sunken."
# •	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not, skip the command. 
# The health of the section cannot exceed the maximum health capacity.
# •	"Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity.
# Print the following:
# "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"
# Input
# •	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# •	On the 2nd line, you are going to receive the status of the warship
# •	On the 3rd line, you will receive the maximum health a section of a ship can reach.
# •	On the following lines, until "Retire", you will be receiving commands.
# Output
# •	Print the output in the format described above.
# Constraints
# •	The section numbers will be integers in the range [1….1000]
# •	The indexes will be integers [-200….200]
# •	The damage will be an integer in the range [1….1000]
# •	The health will be an integer in the range [1….1000]
