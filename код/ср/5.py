def replace_e(tpl, e):
    new_tpl = []
    for i in tpl:
        if i == e:
            new_tpl.append("элемент удалён")
        else:
            new_tpl.append(i)
    return tuple(new_tpl)

print(replace_e((1, 4, 9), 8))
print(replace_e((6, 8, 1, 2, 9, 8, 1, 2), 8))
print(replace_e((1, 2, 8, 5, 1, 2, 9), 8))

