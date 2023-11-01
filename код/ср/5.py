def set_maker(spis):
    new_set = set()
    for i in spis:
        new_set.add(i)
        for x in range(1, spis.count(i)+1):
            new_set.add(str(i)*x)
    return new_set

print(set_maker([1, 1, 3, 3, 1]))
print(set_maker([5, 5, 5, 5, 5, 5, 5]))
print(set_maker([2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]))

