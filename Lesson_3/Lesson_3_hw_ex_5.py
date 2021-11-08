foo_sum = 0


def foo(a):
    list_demo = a.split()
    item_sum = 0
    global foo_sum
    if 'Q' in list_demo:
        index_demo = list_demo.index('Q')
        list_demo.remove('Q')
        for item in list_demo[:index_demo]:
            item_sum += int(item)
        foo_sum += item_sum
        print(foo_sum)
        return
    for item in list_demo:
        item_sum += int(item)
    foo_sum += item_sum
    print(foo_sum)
    foo(input('Числа резделенные пробелом, для выхода введите \'Q\' : '))


foo(input('Числа резделенные пробелом, для выхода введите \'Q\' : '))
