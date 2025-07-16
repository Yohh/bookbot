def get_book_text_words(filepath):
    with open(filepath) as f:
        return f.read().split()

