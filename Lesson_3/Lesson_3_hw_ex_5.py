foo_sum = 0


def foo(a):
    list_demo = a.split()
    item_sum = 0
    gogo = True
    global foo_sum
    if 'Q' in list_demo:
        list_demo.remove('Q')
        gogo = False
    for item in list_demo:
        item_sum += int(item)
    foo_sum += item_sum
    print(foo_sum)
    if not gogo:
        return
    foo(input('Числа резделенные пробелом, для выхода введите \'Q\' : '))


foo(input('Числа резделенные пробелом, для выхода введите \'Q\' : '))
