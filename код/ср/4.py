from memory_profiler import memory_usage

def amount_of_memory_usage(func):
    def wrapper(*args, **kwargs):
        # измеряем количество памяти до выполнения функции
        memory_before = memory_usage()[0]
        # вызываем функцию
        result = func(*args, **kwargs)
        # измеряем количество памяти после выполнения функции
        memory_after = memory_usage()[0]
        amount = (memory_after-memory_before)*1024
        print(f"Функция {func.__name__} занимает {amount} байт памяти")
        return result
    return wrapper

@amount_of_memory_usage
def addition(a,b):
    print(a**b)

@amount_of_memory_usage
def my_list():
    listik = [i for i in range(1, 1000)]
    print(listik)

addition(3, 5)
my_list()