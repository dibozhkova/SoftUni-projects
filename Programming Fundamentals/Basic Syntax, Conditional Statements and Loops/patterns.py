number = int(input())
for line in range(1, number + 1):
    print(line * "*")
for line_down in range(number - 1, -1, -1):
    print(line_down * "*")
