from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text


def main():
    book_text = get_book_text("books/frankenstein.txt")
    words = word_count(book_text)
    return print(words)

main()