def main():
    path_to_book = "books/frankenstein.txt"
    with open(path_to_book) as f:
        file_contents = f.read()

    print_report(file_contents, path_to_book)

def word_count(text):
    count = len(text.split())
    return count

def alpha_string():
    return "abcdefghijklmnopqrstuvwxyz"

def count_chars(text):
    char_counter = {val: 0 for val in alpha_string()}
    for char in text.lower():
        if char in char_counter:
            char_counter[char] += 1

    return sort_count_dict(char_counter)

def sort_count_dict(count_dict):
    return dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))

def print_report(text, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count(text)} words found in the document")
    print("")
    
    for key, val in count_chars(text).items():
        print(f"The '{key}' character was found {val}")
    print("--- End report ---")
    

main()