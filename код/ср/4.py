class NegativeValueException(Exception):
    pass


def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')


if __name__ == '__main__':
    name1 = 'жуля'
    name2 = 'fghjkljhgfdds'
    check_name(name1)
    check_name(name2)