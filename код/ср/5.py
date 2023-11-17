with open('students.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

min_avg_grade = float(input("Введите минимальный средний балл: "))
students = []
for line in lines:
    data = line.strip().split(', ')
    name = data[0]
    age = int(data[1])
    avg_grade = float(data[2])
    if avg_grade > min_avg_grade:
        students.append((name, age, avg_grade))

print("Студенты с средним баллом выше", min_avg_grade, ":")
for student in students:
    print(", ".join(map(str, student)))
