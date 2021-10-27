def expo(a, b):
    if a <= 0:
        print('wololo')
        return
    elif b >= 0:
        print('wololo')
        return
    return a ** b


print(expo(10, -5))


def another_expo(a, b):
    if a <= 0:
        print('wololo')
        return
    elif b >= 0:
        print('wololo')
        return
    i = 0
    y = a
    while i <= (b * -1):
        a = a / y
        i += 1
        # print('wololo')
    return a


print(another_expo(10, -5))
