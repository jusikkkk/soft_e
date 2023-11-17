def longest_words(file):
    with open(file, encoding = 'utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_worlds = word
        if len(sought_worlds) == 1:
            return sought_worlds[0]
        return sought_worlds

print(longest_words('inp.txt'))

