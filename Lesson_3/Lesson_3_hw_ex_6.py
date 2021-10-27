# вариант через title()

# def int_func(a=''):
#     return a.title()
#
#
# print(int_func("wololo wololo wololo wololo"))


def int_func(a=''):
    list_demo = a.split()
    list_demo_copy = []
    for item in list_demo:
        list_demo_copy.append(item[0:1].capitalize() + item[1:])
    return ' '.join(list_demo_copy)


print(int_func(input()))
