from stats import get_num_words, get_num_chars

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in document")
    num_chars = get_num_chars(book_text)
    print(num_chars)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()

