def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = (p*(p-a)*(p-b)*(p-c))**(1/2)
    return area
