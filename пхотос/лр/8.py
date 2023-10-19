value = 5
while value < 100:
    if value % 2 == 0:
        value += 7
    elif value // 5 > 1:
        value *= 5
    else:
        value -= 5