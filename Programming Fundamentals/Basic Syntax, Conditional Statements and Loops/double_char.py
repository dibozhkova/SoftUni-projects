some_string = input()
while some_string != "End":
    if some_string == "SoftUni":
        some_string = input()
    for symbol in some_string:
        print(symbol * 2, end = "")
    print()

    some_string = input()
