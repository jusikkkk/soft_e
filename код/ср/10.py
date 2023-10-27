global result

def rectangle():
    a = float(input("Длина: "))
    b = float(input("Ширина: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("Чтобы вычислить площадь прямоугольника, нажмите 1.\nЧтобы вычислить площадь треугольника, нажмите 2.\n")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")