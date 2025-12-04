def get_word_count(words):
    return len(words.split())

def get_char_count(words):
    words = words.lower()
    char_count = {}
    for char in words:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_char(chars):
    return chars["num"]
def sort_chars(chars):
    rchars = []
    for char in chars:
        rchars.append({"char": char, "num": chars[char]})
    rchars.sort(reverse=True, key=get_char)
    return rchars
