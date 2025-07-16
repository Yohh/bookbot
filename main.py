from stats import get_book_text_words, get_book_stats, sort_list


def main():
    filepath = "books/frankenstein.txt"
    num_words = len(get_book_text_words(filepath))
    char_count = get_book_stats(filepath)
    char_count.sort(key=sort_list, reverse=True)
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_count:
        print(f"{char['char']}: {char['num']}")
    print("============= END ==============")


main()
