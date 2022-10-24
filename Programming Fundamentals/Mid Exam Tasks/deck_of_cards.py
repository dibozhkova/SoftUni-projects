cards_list = input().split(", ")
num_of_commands = int(input())
for _ in range(num_of_commands):
    command = input().split(", ")
    current_command = command[0]
    if current_command == "Add":
        card_name = command[1]
        if card_name not in cards_list:
            cards_list.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif current_command == "Remove":
        card_name = command[1]
        if card_name in cards_list:
            cards_list.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif current_command == "Remove At":
        index = int(command[1])
        if 0 <= index < len(cards_list):
            cards_list.remove(cards_list[index])
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif current_command == "Insert":
        index = int(command[1])
        card_name = command[2]
        if 0 <= index < len(cards_list):
            if card_name in cards_list:
                print("Card is already added")
            else:
                cards_list.insert(index, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")
print(*cards_list, sep=", ")
