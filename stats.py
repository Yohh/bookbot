def get_book_text_words(filepath):
    with open(filepath) as f:
        return f.read().split()


def get_book_stats(filepath):
    with open(filepath) as f:
        text = f.read()
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char]["num"] += 1
            else:
                char_count[char] = {"char": char, "num": 1}
    return list(char_count.values())


def sort_list(items):
    return items["num"]
