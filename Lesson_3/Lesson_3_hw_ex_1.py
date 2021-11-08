def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Wololo'


print(div(int(input('1st num: ')), int(input('2nd num: '))))
