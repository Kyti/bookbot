import sys
from stats import word_count, char_count, sort_chars


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words = word_count(book_text)
    chars = char_count(book_text)
    sorted_chars = sort_chars(chars)
    print_report(book_path, words, sorted_chars)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def print_report(book_path, words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {words} total words")
    print("----------- Character Count -----------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============ END ============")


main()