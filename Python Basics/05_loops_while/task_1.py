book = input()
book_found = ""
book_count = 0

while book != book_found or book_found != "No More Books":
    book_found = input()

    if book_found == "No More Books":
        print(f"The book you search is not here!\nYou checked {book_count} books.")
        break

    if book == book_found:
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1