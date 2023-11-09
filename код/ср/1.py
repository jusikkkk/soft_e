def transformation(inf):
    a = inf.split(" ")
    return a
if __name__ == "__main__":
    information = input("Введите последовательность чисел через пробел : ")
    print(list(transformation(information)))
    print(tuple(transformation(information)))
