def count_words(text):
    word_array = text.split()
    word_count = len(word_array)
    return word_count

def count_letters(text):
    book_stats = {}
    for letter in text:
        letter = letter.lower()
        book_stats[letter] = book_stats.get(letter, 0) + 1

    return book_stats

def sort_on(items):
    return items["num"]

def sort_dict(dictonary):
    sorted_list = []
    for key, value in dictonary.items():
        sorted_list.append(
            {"char": key,
             "num": value}
        )
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list