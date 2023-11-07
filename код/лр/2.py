from pprint import pprint

my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a = 78, b = 45, c = 90, d = 59)
dict_maker(name = "Олежа", age = 28, weight = 86, eyes_color = "green")
pprint(my_dict)