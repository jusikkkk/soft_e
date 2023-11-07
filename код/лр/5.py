def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((7, 1, 0, 34, 21)))
    print(tuple_sort((7, 1, '24', 0, 34, 21)))