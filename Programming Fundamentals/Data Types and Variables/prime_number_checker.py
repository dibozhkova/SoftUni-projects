number = int(input())
count = 0

if number > 1:
    for num in range(1, number + 1):
        if number % num == 0:
            count += 1
    if count == 2:
        print("True")
    else:
        print("False")
