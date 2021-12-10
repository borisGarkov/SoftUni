words_collection = input().split()


def swap_words(words_collection, word_1, word_2):
    if word_1 in words_collection and word_2 in words_collection:
        index_1 = words_collection.index(word_1)
        index_2 = words_collection.index(word_2)

        words_collection[index_1], words_collection[index_2] = words_collection[index_2], words_collection[index_1]
    return words_collection


def put_word_at_index(words_collection, word, index_word):
    if index_word - 1 in range(len(words_collection) + 1):
        words_collection.insert(index_word - 1, word)
    return words_collection


def replace_word(words_collection, word_1, word_2):
    if word_2 in words_collection:
        index_word = words_collection.index(word_2)
        words_collection[index_word] = word_1
    return words_collection


while True:
    data = input()
    if data == "Stop":
        break

    if data == "Sort":
        words_collection.sort(reverse=True)
    elif data.split()[0] == "Delete":
        index = data.split()[1]
        index = int(index)

        if index + 1 in range(len(words_collection)):
            words_collection.pop(index + 1)
    else:
        command, first_element, second_element = data.split()

        if command == "Swap":
            words_collection = swap_words(words_collection, first_element, second_element)
        elif command == "Put":
            second_element = int(second_element)
            words_collection = put_word_at_index(words_collection, first_element, second_element)
        elif command == "Replace":
            words_collection = replace_word(words_collection, first_element, second_element)

print(*words_collection)
