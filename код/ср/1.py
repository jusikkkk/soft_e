with open('ukf.txt', encoding='utf-8') as f:
    w_count = 0
    article_line = f.read().split()
    for words in article_line:
        w_count += 1

print(w_count)
