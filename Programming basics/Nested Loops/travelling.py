destination = input()

while destination != "End":
    needed_money = float(input())
    save_money = 0
    while save_money < needed_money:
        current_money = float(input())
        save_money += current_money
    print(f"Going to {destination}!")
    destination = input()
