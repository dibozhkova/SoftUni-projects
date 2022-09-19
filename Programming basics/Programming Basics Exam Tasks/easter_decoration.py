clients_num = int(input())

total_bill = 0
for client in range(1, clients_num + 1):
    bill = 0
    count_item = 0
    product = input()
    while product != "Finish":
        if product == "basket":
            bill += 1.5
            count_item += 1
        elif product == "wreath":
            bill += 3.8
            count_item += 1
        elif product == "chocolate bunny":
            bill += 7
            count_item += 1

        product = input()
    if count_item % 2 == 0:
        bill *= 0.8
        total_bill += bill
    else:
        total_bill += bill
    print(f"You purchased {count_item} items for {bill:.2f} leva.")
    if client == clients_num:
        avr_bill = total_bill / clients_num
        print(f"Average bill per client is: {avr_bill:.2f} leva.")
