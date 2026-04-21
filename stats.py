def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    char_count = {}

    for char in book_text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]

def get_sorted_chars(num_chars_dict):
    sorted = []
    for char,count in num_chars_dict.items():
        sorted.append({"char": char, "num": count})
    sorted.sort(reverse=True,key=sort_on)
    return sorted

        
    



