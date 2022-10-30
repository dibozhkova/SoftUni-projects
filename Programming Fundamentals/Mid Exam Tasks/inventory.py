items = input().split(", ")
line_input = input().split(" - ")
command = line_input[0]
while line_input[0] != "Craft!":
    command = line_input[0]
    if command == "Collect":
        item = line_input[1]
        if item not in items:
            items.append(item)
    elif command == "Drop":
        item = line_input[1]
        if item in items:
            items.remove(item)
    elif command == "Combine Items":
        combine_items = line_input[1].split(":")
        old_item = combine_items[0]
        new_item = combine_items[1]
        if old_item in items:
            index_of_old_item = items.index(old_item)
            items.insert(index_of_old_item + 1, new_item)
    elif command == "Renew":
        item = line_input[1]
        if item in items:
            items.append(items.pop(items.index(item)))
    line_input = input().split(" - ")
print(*items, sep=", ")



# You will receive a journal with some collecting items, separated with a comma and a space (", ").
# After that, until receiving "Craft!" you will be receiving different commands split by " - ":
# •	"Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this line.
# •	"Drop - {item}" - you should remove the item from your inventory if it exists.
# •	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
# •	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", ".
