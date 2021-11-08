import itertools
from sys import argv

script_demo, num = argv


def foo(a):
    for el in itertools.count(a):
        if el > 100:
            break
        print(el)


foo(int(num))
