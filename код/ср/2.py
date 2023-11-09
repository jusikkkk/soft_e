def element_delete(args, element):
    tuple_to_list = list(args)
    for i in tuple_to_list:
        if i == element:
            tuple_to_list.remove(i)
            break
    return tuple(tuple_to_list)

print(element_delete((1, 2, 3), 1))
print(element_delete((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(element_delete((2, 4, 6, 6, 4, 2), 9))
