def useless(lst):
    return max(lst) / len(lst)

print(useless([3, 9, 22, 8, 3]))
print(useless([45, 2.0, 0, -45.2, 84, 102.6, 308]))
print(useless([901, 35.2, 120, 1056.3]))