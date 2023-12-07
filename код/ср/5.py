class MyException(Exception):
    pass

def divide(a, b): 
    if b == 0:
        raise MyException("На ноль делить нельзя!")
    return a / b

try:
    result = divide(10, 0)
except MyException as e:
    print(e)
else:
    print(result)

def call_centre(phone_number):
    if len(phone_number) != 11:
        raise MyException("Номер введен некорректно!")
    else:
        print(f"Вы звоните на номер {phone_number}")

try:
    pn = call_centre("898274661992")
except MyException as e:
    print(e)
else:
    pn

try:
    pn = call_centre("89193756122")
except MyException as e:
    print(e)
else:
    pn