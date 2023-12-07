import time

def prog_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\nВыполнение функции {func.__name__} занимает {end_time - start_time} секунд")
        return result
    return wrapper

@prog_time
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')

if __name__ == '__main__':
    fibonacci()