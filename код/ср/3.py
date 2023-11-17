with open('input.txt','r') as f:
    line = f.readlines()
    c_lines = 0
    c_words = 0
    c_letters = 0
    for lines in line:
        c_lines += 1
    for lines in line:
        word = lines.split(' ')
        c_words += len(word)
        for words in word:
            letters = list(words)
            c_letters += len(letters)
    print(f"Input file contains:\n{c_letters-7} letters\n{c_words} words\n{c_lines} lines")
