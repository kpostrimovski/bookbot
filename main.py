from stats import count_words, count_letters, sort_dict
import sys


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    frank = get_book_text(filepath)
    word_count = count_words(frank)
    book_stats = count_letters(frank)
    sorted_book_stats = sort_dict(book_stats)
    print_all(filepath,word_count, sorted_book_stats)


def get_book_text (filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents

def print_all(filepath,word_count, sorted_book_stats):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"----------- Character Count ----------")
    for character in sorted_book_stats:
        print(f"{character["char"]}: {character["num"]}")


main()