key = int(input())
line_input = int(input())
for symbol in range(line_input):
    letter = input()
    value_letter = ord(letter)
    messages = chr(value_letter + key)
    print(f"{messages}", end = "")
