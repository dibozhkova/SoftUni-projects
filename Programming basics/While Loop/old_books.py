wanted_book = input()

count_books = 0
while wanted_book != "No More Books":
    current_book = input()
    if current_book != wanted_book:
        count_books += 1
    else:
        print(f"You checked {count_books} books and found it.")
        break
    if current_book == "No More Books":
        count_books -= 1
        print("The book you search is not here!")
        print(f"You checked {count_books} books.")
        break
