def addition(num):
    try:
        if num is float or int:
            print(2+num)
    except TypeError:
        print("Введён неверный тип данных")

addition(6)
addition("шесть")