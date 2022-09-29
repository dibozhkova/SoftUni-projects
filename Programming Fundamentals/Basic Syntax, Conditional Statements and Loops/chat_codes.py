number = int(input())
for numbers in range(1, number + 1):
    current_num = int(input())
    if current_num == 88:
        print("Hello")
    elif current_num == 86:
        print("How are you?")
    elif current_num < 88:
        if current_num != 88 or current_num != 86:
            print("GREAT!")
    elif current_num > 88:
        print("Bye.")
