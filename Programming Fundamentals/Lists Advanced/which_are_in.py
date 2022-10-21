# You will be given two sequences of strings, separated by ", ". 
# Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.


first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_sequence = []
for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word and not first_word in new_sequence:
            new_sequence.append(first_word)
print(new_sequence)
