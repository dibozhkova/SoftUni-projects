film_name = input()
type_room = input()
tickets_num = int(input())
price_ticket = 0
if film_name == "A Star Is Born":
    if type_room == "normal":
        price_ticket = 7.5
    elif type_room == "luxury":
        price_ticket = 10.5
    elif type_room == "ultra luxury":
        price_ticket = 13.5
elif film_name == "Bohemian Rhapsody":
    if type_room == "normal":
        price_ticket = 7.35
    elif type_room == "luxury":
        price_ticket = 9.45
    elif type_room == "ultra luxury":
        price_ticket = 12.75
elif film_name == "Green Book":
    if type_room == "normal":
        price_ticket = 8.15
    elif type_room == "luxury":
        price_ticket = 10.25
    elif type_room == "ultra luxury":
        price_ticket = 13.25
elif film_name == "The Favourite":
    if type_room == "normal":
        price_ticket = 8.75
    elif type_room == "luxury":
        price_ticket = 11.55
    elif type_room == "ultra luxury":
        price_ticket = 13.95
total_sum = tickets_num * price_ticket
print(f"{film_name} -> {total_sum:.2f} lv.")
