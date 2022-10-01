some_string = input().lower()
list_of_words = ["sand", "water", "fish", "sun"]
counter_words = 0
for word in list_of_words:
    if word in some_string:
        word_count = some_string.count(word)
        counter_words += word_count
print(counter_words)
