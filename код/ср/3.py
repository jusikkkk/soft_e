def slowarik(str):
    diction = {}
    if len(str) < 15:
        print("Введено недостаточное количество символов")
        exit()
    else:
        for i in str:
            key = i
            diction[key] = str.count(i)
    sorted_dict = dict(sorted(diction.items(), key=lambda x: x[1], reverse=True))
    dict_slice = dict(list(sorted_dict.items())[0:3])
    return dict(sorted(dict_slice.items()))

print(slowarik("88881232833344611"))
print(slowarik("13912"))




