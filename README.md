# Тема 4 . ...
Отчет по Теме # выполнил(а):
- Ознобихина Юлия Дмитриевна
- АИС-21-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |   |
| Задание 7 | + |   |
| Задание 8 | + |   |
| Задание 9 | + |   |
| Задание 10 | + |   |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Выведите в консоль три строки. Первая – любое число. Вторая – любое число в виде строки. Третья – любое число с плавающей точкой.

```python
import random
def main():
    chiselka = random.randint(1, 6)
    print( f"Ваше значение: {chiselka}")
    if chiselka in [1, 2]:
        print("Вы проиграли(((")
    elif chiselka in [3,4]:
        main()
    else:
        print("Вы выиграли!")

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/1.PNG)

## Выводы

В данном коде выводятся три строки с использованием функции `print()`. Каждая строка содержит разные значения:

1. `print(123)`: Выводится целое число 123. Это число не взаимодействует со строковыми операциями и выводится как есть.

2. `print('123')`: Выводится строка '123', так как она заключена в одинарные кавычки. В этом случае это текстовая строка, а не число.

3. `print(1.23)`: Выводится число с плавающей точкой 1.23. Так же, как и в первом случае, оно выводится как числовое значение.

## Лабораторная работа №2
- Текст задания
```python
def main():
    result = 12 * 98
    return result

if __name__ == '__main__':
    ans = main()
    print(ans)
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/2.PNG)
## Выводы

## Лабораторная работа №3
- Текст задания
```python
def main(a, b):
    result = (a ** b)//2
    return(result)

for i in range(7):
    first = 2
    second = 8
    answ = main(first, second)
    print(answ)
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/3.PNG)
## Выводы
  
## Лабораторная работа №4
- Текст задания
```python
def main(x, *args):
    one = x # 4
    two = args # 0, 2, 4, -8, -7, 15, 2, -4, -3
    three = sum(two) # cумма элементов кортежа args
    four = float(len(two)) # длина кортежа args
    # построчный вывлд переменных и их значений
    print(f"one = {one}\ntwo = {two}\nthree = {three}\nfour = {four}")
    return one + three / four

if __name__ == '__main__':
    result = main(4, 0, 2, 4, -8, -7, 15, 2, -4, -3)
    print(f"\nresult={result}")
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/4.PNG)
## Выводы

## Лабораторная работа №5
- Текст задания
```python
def main(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(**{'x': [0, 4, 1, 6], 'y': [3, 0, 2, 9], 'z': [4, 6, 0, 3], 'q': [7, 8, 1, 0]})
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/5.PNG)
## Выводы

## Лабораторная работа №6
- Текст задания
```python
def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return(sum(data) / float(len(data)))

if __name__ == '__main__':
    main(x = [1, 4, 7], y = [2, 5, 8], z = [3, 6, 9], q = [4, 7, 10])
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/6.PNG)
## Выводы

## Лабораторная работа №7
- Текст задания
## код основной программы
```python
from for_import7 import importnaya

if __name__ == '__main__':
    importnaya()
```
## код импортируемой программы:
```python
def importnaya():
    print("уъу")
```

### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/7.1.PNG)
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/7.2.PNG)
## Выводы

## Лабораторная работа №8
- Текст задания
```python
from math import sqrt, sin, cos

def main():
    ciferka = int(input('Введите значение:'))
    print("Корень значения: ", sqrt(ciferka))
    print("Синус значения: ", sin(ciferka))
    print("Коcинус значения: ", cos(ciferka))

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/8.PNG)
## Выводы

## Лабораторная работа №9
- Текст задания
```python
from datetime import datetime as dati
from datetime import timedelta as dt

def main():
    print(
        f"Сегодня {dati.today().date()}."
        f"День недели - {dati.today().isoweekday()}"
    )
    n = int(input("Введите количество дней: "))
    today = dati.today()
    result = today + dt(days=n)
    print(
        f"Через {n} дней будет {result.date()}."
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/9.PNG)
## Выводы

## Лабораторная работа №10
- Текст задания
```python
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
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D0%BB%D1%80/10.PNG)
## Выводы

## Самостоятельная работа №1
- Текст задания
```python
from datetime import datetime # из библиотеки datetime импортируем класс datetime, позволяющий управлять значениями даты и времени одновременно
from math import sqrt # из библиотеки math импортируем функцию изъятия корня sqrt

def main(**kwargs):
    '''
    Функция main на вход получает словарь kwargs.
    Цикл for проходит работает с парами ключ-значение по ключам (one, two, three и т.д)
    Args:
        result (float): переменная, принимающая значение корня из суммы квадратов
        key[i][j] (int) : i - номер строки, j - номер позиции элемента в строке
    Returns:
        result(float)

    '''
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # извлекаем корень из суммы квадратов
        print(result)

if __name__ == '__main__': ## точка входа

    start_time = datetime.now() # переменная start_time принимает значение текущего времени (время начала работы программы)


    main( #функция main и её аргументы
        one = [10, 3],
        two = [5, 4],
        three =[15, 13],
        four = [93, 53],
        five = [133, 15]

    )


    time_costs = datetime.now() - start_time # вычисляем время выполнения косманды как разницу времени конца работы программы и start_time
    print(f"Время выполнения программы - {time_costs}") #выводим f-строку с переменной time_costs
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D1%81%D1%80/1.PNG)
## Выводы
  
## Самостоятельная работа №2
- Текст задания
```python
import random
def main():
    chiselka = random.randint(1, 6)
    print( f"Ваше значение: {chiselka}")
    if chiselka in [1, 2]:
        print("Вы проиграли(((")
    elif chiselka in [3,4]:
        main()
    else:
        print("Вы выиграли!")

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D1%81%D1%80/2.1.PNG)
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D1%81%D1%80/2.2.PNG)
## Выводы
  
## Самостоятельная работа №3
- Текст задания
```python
import datetime as d
import time as t

star_t = t.time()
end_t = star_t + 5
while t.time() < end_t:
    print(d.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    t.sleep(1)
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D1%81%D1%80/3.PNG)
## Выводы
  
## Самостоятельная работа №4
- Текст задания
```python
def main(*args):
    n = len(args)
    summ = sum(args)
    average = summ / n
    print(average)

if __name__ == '__main__':
    main(2,5,8,10,62,101)
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D1%81%D1%80/4.PNG)
## Выводы
  
## Самостоятельная работа №5
- Текст задания
## код импортируемой программы
```python
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return area
```
## код основной программы
```python
from heron import triangle_area
print(triangle_area(int(input("Ведите длину строны a: ")),
                    int(input("Ведите длину строны b: ")),
                    int(input("Ведите длину строны c: "))))
```
### Результат.
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D1%81%D1%80/5.1.PNG)
![Меню](https://github.com/jusikkkk/soft_e/blob/%D0%A2%D0%B5%D0%BC%D0%B0_4/%D0%BF%D0%B8%D0%BA%D1%87%D0%B8/%D1%81%D1%80/5.2.PNG)
## Выводы
  

## Общие выводы по теме
- Развернутый вывод

