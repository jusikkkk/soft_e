def main(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(**{'x': [0, 4, 1, 6], 'y': [3, 0, 2, 9], 'z': [4, 6, 0, 3], 'q': [7, 8, 1, 0]})