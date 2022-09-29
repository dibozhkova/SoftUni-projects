number = int(input())
for string in range(number):
    some_string = input()
    if "," in some_string or "." in some_string or "_" in some_string:
        print(f"{some_string} is not pure!")
    else:
        print(f"{some_string} is pure.")
