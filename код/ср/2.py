def isempty(file_name):
    try:
        with open(file_name, "r", encoding='utf-8') as f:
            data = f.read()
            if not data:
                raise Exception("Файл пустой!")
            print(data)

    except Exception as e:
        print(e)

isempty('empty.txt')
isempty('not_empty.txt')
