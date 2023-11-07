request = int(input("Введите номер кабинета : "))

directionary = {
    235: {'key' : 7823, 'access' : True},
    105: {'key' : 9874, 'access' : True},
    415: {'key' : 3453, 'access' : False},
    551: {'key' : 1987, 'access' : True},
    None: {'key' : None, 'access' : False},
}

response = directionary.get(request)
if not response:
    response = directionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)