def get_book_text_words(filepath):
    with open(filepath) as f:
        return f.read().split()


def get_book_stats(filepath):
    with open(filepath) as f:
        text = f.read()
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
