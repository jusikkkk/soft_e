def chiter(lst):
    new_grade = []
    for grade in lst:
        if grade == 2:
            continue
        elif grade == 3:
            new_grade.append(4)
        else:
            new_grade.append(grade)
    return new_grade

print(chiter([2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]))
print(chiter([4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]))
print(chiter([5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]))