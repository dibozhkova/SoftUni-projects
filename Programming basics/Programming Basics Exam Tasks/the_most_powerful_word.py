import math
import sys

line_input = input()
max_word = -sys.maxsize
best_word = ""
while line_input != "End of words":
    word = line_input
    value = 0
    for letter in word:
        value += ord(letter)
        first_letter = word[0]
        len_word = len(word)
    if first_letter == "A" or first_letter == "E" or first_letter == "I" \
            or first_letter == "O" or first_letter == "U" or first_letter == "Y"\
            or first_letter == "a" or first_letter == "e" or first_letter == "i"\
            or first_letter == "o" or first_letter == "u" or first_letter == "y":
        value *= len_word
    else:
        value = math.ceil(value / len_word)
    if value > max_word:
        max_word = value
        best_word = word

    line_input = input()
print(f"The most powerful word is {best_word} - {max_word}")
