number_of_lines = int(input())
sum_of_chars = 0
for letter in range(1, number_of_lines + 1):
    current_letter = input()
    sum_of_chars += ord(current_letter)
print(f"The sum equals: {sum_of_chars}")
