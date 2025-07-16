def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_book_text_words(filepath):
    with open(filepath) as f:
        return f.read().split()


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = len(get_book_text_words(filepath))
    print(f"{num_words} words found in the document")


main()
