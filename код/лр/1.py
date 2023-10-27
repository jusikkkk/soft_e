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