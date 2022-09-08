number = int(input())

counter = 1
is_bigger_n = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if counter > number:
            is_bigger_n = True
            break
        print(counter, end = " ")
        counter += 1
    if is_bigger_n:
        break
    print()
