def count_words(text):
    words=text.split()
    return len(words)

def count_characters(text):
    text=text.lower()
    chars={}
    for char in text:
        if char in chars:
            chars[char] +=1
        else:
            chars[char] = 1
    return chars

def sort_characters(char_dict):
    char_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})

    def sort_on(d):
        return d["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list
