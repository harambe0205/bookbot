def get_num_words(text):
    words = str.split(text)
    return len(words)

def get_num_characters(text):
    lower = str.lower(text)
    letter_count = {}
    for letter in lower:
       if letter in letter_count:
          letter_count[letter] += 1
       else:
          letter_count[letter] = 1
    return letter_count

def sort_on(item):
    return item["num"]

def build_sorted_list(letter_count):
    sort_list = []
    for character, count in letter_count.items():
        sort_list.append({"char": character, "num": count})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    
