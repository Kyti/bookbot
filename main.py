# main function
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = character_count(text)
    sorted_chars = sort_character_count(chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char, count in sorted_chars:
        print(f"The '{char}' was found {count} times.")
    


# word count
def get_num_words(text):
    words = text.split() # splitting the string into a list of words
    return len(words) # returning the length of the word list


# finding the book and opening in read mode
def get_book_text(path):
    with open(path) as f:
        return f.read()


# counting how many times each character appears
def character_count(text):
    char_dict = {} # creating a dictionary to store each character and the count
    lowered_text = text.lower() # converting the text to lowercase so capital/lowercase are not two counts
    for char in lowered_text: # looping through each character
        if char in char_dict: # add to existing keys
            char_dict[char] += 1
        else:
            char_dict[char] = 1 # create new keys if they don't exist and count 1
    return char_dict

# sorting characters by count and filtering non-alpha
def sort_character_count(char_dict):
    alpha_chars = {char: count for char, count in char_dict.items() if char.isalpha()} # sorts out only alphabetical characters
    return sorted(alpha_chars.items(), key=lambda x: x[1], reverse=True)
    


main()
