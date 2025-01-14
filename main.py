def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sort_list = dict_sort(character_count)

    print(f"=== Begin Report of {book_path} ===")
    print(f"{word_count} words found in the document")
    print()

    for i in sort_list:
        if i["letter"].isalpha():
            print(f"The {i["letter"]} character was found {i["num"]} times")

    print("=== End Report ===")


def letter_sort(i):
    return i["num"]

def dict_sort(text):
    new_list = []
    for i in text:
        new_list.append({"letter": i, "num": text[i]})
    new_list.sort(reverse=True, key=letter_sort)
    return new_list
    
def get_character_count(text):
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