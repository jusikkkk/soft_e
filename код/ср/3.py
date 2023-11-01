one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return area

a1, b1, c1 = max(one), max(two), max(three)
a2, b2, c2 = min(one), min(two), min(three)

print("Треугольник максимальных сторон : ", triangle_area(a1, b1, c1))
print("Треугольник минимальных сторон : ", triangle_area(a2, b2, c2))
