import sys
from stats import (
    get_num_words, 
    get_num_chars, 
    get_sorted_chars
)

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        num_chars = get_num_chars(book_text)
        sorted_chars = get_sorted_chars(num_chars)
        print_report(book_path, num_words, sorted_chars)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def print_report(book_path,num_words,sorted_chars):
    print("======== BOOKBOT REPORT ========")
    print(f"Analyzing book found at {book_path}")
    print("-------- Word Count --------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============ END ============")

main()