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


