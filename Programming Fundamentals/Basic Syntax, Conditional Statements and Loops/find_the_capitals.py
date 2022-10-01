word = input()
list_of_capital_letter = []
for index in range(len(word)):
    if word[index].isupper():
        list_of_capital_letter.append(index)
print(list_of_capital_letter)
