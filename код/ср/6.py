def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return(sum(data) / float(len(data)))

if __name__ == '__main__':
    main(x = [1, 4, 7], y = [2, 5, 8], z = [3, 6, 9], q = [4, 7, 10])