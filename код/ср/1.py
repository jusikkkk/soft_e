with open('ukf.txt', encoding='utf-8') as f:
    w_count = 0
    article_line = f.read().split()
    word_count = {}
    for word in article_line:
        if len(word)>2 and word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for words in article_line:
        w_count += 1
    most_common_word = max(word_count, key=word_count.get)

print(f"Количество слов: {w_count}\nНаиболее часто встречающееся слово: {most_common_word}")
