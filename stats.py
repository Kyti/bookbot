def word_count(book_text):
    text = str(book_text)
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return print(f"{count} words found in the document")