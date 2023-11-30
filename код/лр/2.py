def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name, age)

    return output_func

@check
def personal_info(name, age):
    print(f"Name:{name}  Age:{age}")

if __name__ == '__main__':
    personal_info('Александр', 56)
    personal_info('Максим', -3)
    personal_info('Олег', 18, 152, 1, -112)