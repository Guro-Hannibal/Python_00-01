def sum_biggest_2(a, b, c):
    if (a >= b or a >= c) and (b >= c or b >= a):
        return a + b
    elif (c >= a or c >= b) and (a >= b or a >= c):
        return c + a
    elif (b >= c or b >= a) and (c >= a or c >= b):
        return b + c


print(sum_biggest_2(19, 11, 15))
