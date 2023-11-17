def expenses(file):
    with open(file, 'w', encoding='utf-8') as f:
        i = int(input("Введите количество расходов : "))
        for i in range(1, i+1):
            exspense = input('Введите название расхода : ')
            amount = input('Введите сумму : ')
            f.write(f'{exspense} - {amount} руб\n')

    with open(file, 'r', encoding='utf-8') as f:
        book = f.readlines()
        for line in book:
            print(line)

print(expenses('exp.txt'))
