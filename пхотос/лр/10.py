e_array = [2, 5, 6, 9, 12]
flag = False
for value in e_array:
    if value % 2 == 1:
        flag = True
if flag is True:
    print('В массиве есть нечетное число')
else:
    print('В массиве все числа четные')