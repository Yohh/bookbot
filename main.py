from stats import get_book_text_words
from stats import get_book_stats


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = len(get_book_text_words(filepath))
    char_count = get_book_stats(filepath)
    print(f"{num_words} words found in the document")
    print(char_count)


main()
