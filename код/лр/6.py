with open('лаба.txt', 'a+') as f:
    f.write('\nIm additiomal line')

with open('лаба.txt', 'r') as f:
    result = f.readlines()
    print(result)