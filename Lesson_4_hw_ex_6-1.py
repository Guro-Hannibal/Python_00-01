from itertools import cycle
import sys

script_demo, range_end, break_count = sys.argv

list_demo = [el for el in range(5, int(range_end), 5) if str(el)[-1] == '5']


def foo(a):
    i = 0
    for el in cycle(list_demo):
        print(el)
        i += 1
        if i > a:
            break


foo(int(break_count))
