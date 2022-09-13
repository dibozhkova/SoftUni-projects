num_moves = int(input())

result = 0
result1 = 0
result2 = 0
result3 = 0
result4 = 0
result5 = 0
result6 = 0

for i in range(1, num_moves + 1):
    number = int(input())
    if 0 <= number <= 9:
        result = result + number * 0.2
        result1 = result1 + 1
    elif 10 <= number <= 19:
        result = result + number * 0.3
        result2 = result2 + 1
    elif 20 <= number <= 29:
        result = result + number * 0.4
        result3 = result3 + 1
    elif 30 <= number <= 39:
        result = result + 50
        result4 = result4 + 1
    elif 40 <= number <= 50:
        result = result + 100
        result5 = result5 + 1
    else:
        result = result / 2
        result6 = result6 + 1

print(f"{result:.2f}")
print(f"From 0 to 9: {result1 / num_moves * 100:.2f}%")
print(f"From 10 to 19: {result2 / num_moves * 100:.2f}%")
print(f"From 20 to 29: {result3 / num_moves * 100:.2f}%")
print(f"From 30 to 39: {result4 / num_moves * 100:.2f}%")
print(f"From 40 to 50: {result5 / num_moves * 100:.2f}%")
print(f"Invalid numbers: {result6 / num_moves * 100:.2f}%")
