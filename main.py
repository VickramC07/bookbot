import sys

from stats import get_word_count
from stats import get_char_count
from stats import sort_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    wc = get_word_count(text)
    char_counts = get_char_count(text)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_chars(char_counts)
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()
