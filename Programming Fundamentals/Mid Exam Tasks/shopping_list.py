groceries = input().split("!")
line_input = input()
while line_input != "Go Shopping!":
    command = line_input.split()
    if command[0] == "Urgent":
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif command[0] == "Unnecessary":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
    elif command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries:
            groceries = groceries[:groceries.index(old_item)] + [new_item] + groceries[groceries.index(old_item) + 1:]
    elif command[0] == "Rearrange":
        item = command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    line_input = input()
print(*groceries, sep=", ")



# It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
# Input
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.
# Constraints
# •	There won't be any duplicate items in the initial list
# Output
# •	Print the list with all the groceries, joined by ", ":
# "{firstGrocery}, {secondGrocery}, … {nthGrocery}"
