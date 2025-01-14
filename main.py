def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    print(letter_count)

def get_letter_count(text):
    string = {}
    for i in text.lower():
        if i in string:
            string[i] += 1
        else:
            string[i] = 1
    return string

def get_word_count(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()