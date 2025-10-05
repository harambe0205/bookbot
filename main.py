import sys
from stats import get_num_words, get_num_characters, sort_on, build_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    letter_count = get_num_characters(text)
    print(f"Found {word_count} total words")
    sorted_chars = build_sorted_list(letter_count)
    for entry in sorted_chars:
        ch = entry["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {entry['num']}")
main()
