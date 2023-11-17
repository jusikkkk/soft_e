def censor_sentence(sentence, banned_list):
    words = sentence.split()
    censored_words = list()
    for word in words:
        l_word = word.lower()
        for f_word in banned_list:
            if (l_word.find(f_word) >= 0):
                b_word = l_word.replace(f_word, '*' * len(f_word))
                censored_words.append(b_word)
                break
        else:
            censored_words.append(word)
    censored_sentence = ' '.join(censored_words)
    print(censored_sentence)

with open('banned.txt', 'r', encoding='utf-8') as file:
    banned_w = file.read().split()

sentence = "Hello, world ! Python IS the programming language of thE future. My EMAIL is .... PYTHON is awesome!!!!"
censor_sentence(sentence, banned_w)