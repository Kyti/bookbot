def word_count(book_text):
    words = book_text.split()
    return len(words)


def char_count(book_text):
    chars = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def sort_chars(chars_dict):
    sorted = []
    for char in chars_dict:
        sorted.append({"char": char, "num": chars_dict[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted