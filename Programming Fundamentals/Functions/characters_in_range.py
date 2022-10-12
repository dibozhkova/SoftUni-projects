# Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code), separated by a single space. Print the result on the console.


def el_between_char(char1, char2):
    collected_char = []
    for current_char in range(ord(char1) + 1, ord(char2)):
        collected_char.append(chr(current_char))
    return collected_char

first_char = input()
second_char = input()
result = el_between_char(first_char, second_char)
print(" ".join(result))
