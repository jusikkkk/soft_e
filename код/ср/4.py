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
