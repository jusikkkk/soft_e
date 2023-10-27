def main(*args):
    n = len(args)
    summ = sum(args)
    average = summ / n
    print(average)

if __name__ == '__main__':
    main(2,5,8,10,62,101)
