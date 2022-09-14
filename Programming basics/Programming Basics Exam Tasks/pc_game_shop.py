sold_games = int(input())
hearthstone_count = 0
fornite_count = 0
overwach_count = 0
others_count = 0
for games in range(1, sold_games + 1):
    name_game = input()
    if name_game == "Hearthstone":
        hearthstone_count += 1
    elif name_game == "Fornite":
        fornite_count += 1
    elif name_game == "Overwatch":
        overwach_count += 1
    else:
        others_count += 1
hearthstone_percent = hearthstone_count / games * 100
print(f"Hearthstone - {hearthstone_percent:.2f}%")
fornite_percent = fornite_count / games * 100
print(f"Fornite - {fornite_percent:.2f}%")
overwach_percent = overwach_count / games * 100
print(f"Overwatch - {overwach_percent:.2f}%")
others_percent = others_count / games * 100
print(f"Others - {others_percent:.2f}%")
