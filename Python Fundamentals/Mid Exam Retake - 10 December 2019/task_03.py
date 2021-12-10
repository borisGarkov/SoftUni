books = input().split("&")


def case_add_book(books_list, book):
    if book not in books_list:
        books_list.insert(0, book)
    return books_list


def case_remove_book(books_list, book):
    if book in books_list:
        books_list.remove(book)
    return books_list


def case_swap_books(books_list, book_1, book_2):
    if book_1 in books_list and book_2 in books_list:
        book_1_position = books_list.index(book_1)
        book_2_position = books_list.index(book_2)
        books_list[book_1_position], books_list[book_2_position] = \
            books_list[book_2_position], books_list[book_1_position]
    return books_list


def case_insert_book(books_list, book):
    books_list.append(book)
    return books_list


def case_check_book(books_list, index):
    if index in range(0, len(books_list)):
        print(books_list[index])


while True:
    command = input()
    if command == "Done":
        break

    if command.split(" | ")[0] != "Swap Books":
        action, book_name = command.split(" | ")
    else:
        action, book_1, book_2 = command.split(" | ")

    if action == "Add Book":
        books = case_add_book(books, book_name)
    elif action == "Take Book":
        books = case_remove_book(books, book_name)
    elif action == "Swap Books":
        books = case_swap_books(books, book_1, book_2)
    elif action == "Insert Book":
        books = case_insert_book(books, book_name)
    elif action == "Check Book":
        case_check_book(books, int(book_name))

print(", ".join(books))
