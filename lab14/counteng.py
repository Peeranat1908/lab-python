def count_char(word):
    char_count = {}
    word = word.lower()
    for i in word:
        if i.isalpha() and i.islower():
            if i not in char_count:
                char_count[i] = 1
            else:
                char_count[i] += 1
    return char_count

print(count_char('Hello, There'))