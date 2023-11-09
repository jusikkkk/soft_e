def last_index(str, a):
    indexes = list()
    last_i = 0
    for i in range (len(str)):
        if str[i] == a:
            indexes.append(i)
    if len(indexes) == 1:
        last_i = None
    else:
        last_i = indexes[1]+1
    return last_i

def kakayato(empl_id, id):
    outout = tuple()
    if id not in empl_id:
        return ()
    else:
        first_i = empl_id.index(id)
        last_i = last_index(empl_id, id)
        outout = empl_id[first_i:last_i]
    return outout

print(kakayato((1, 2, 3), 8))
print(kakayato((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(kakayato((1, 2, 8, 5, 1, 2, 9), 8))





