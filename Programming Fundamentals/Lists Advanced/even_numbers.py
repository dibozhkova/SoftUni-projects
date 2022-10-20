# Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.


numbers = [int(el) for el in input().split(", ")]
print([index for index in range(len(numbers)) if numbers[index] % 2 == 0])
