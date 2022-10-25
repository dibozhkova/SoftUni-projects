elements = input().split()
line_input = input()
moves = 0
while line_input != "end":
    moves += 1
    index1, index2 = [int(i) for i in line_input.split()]
    if not 0 <= index1 < len(elements) or not 0 <= index2 < len(elements) or index1 == index2:
        elements.insert(len(elements) // 2, f"-{moves}a")
        elements.insert(len(elements) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[index1] == elements[index2]:
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            matching_element = elements.pop(index1)
            elements.remove(matching_element)
        else:
            print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

    line_input = input()

if line_input == "end" and len(elements) > 0:
    print("Sorry you lose :(")
    print(*elements, sep=" ")

    
# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. 
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space, representing the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, 
# you should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a" 
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line, you will receive a sequence of elements
# •	On the following lines, you will receive integers until the command "end"
# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
# "Congrats! You have found matching elements - ${element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console the following message: 
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# •	All elements in the sequence will always have a matching element.
