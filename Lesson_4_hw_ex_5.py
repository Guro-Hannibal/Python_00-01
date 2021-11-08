from functools import reduce


list_demo = [el for el in range(100, 1001) if el % 2 == 0]


def foo(a, b):
    return a * b


print(reduce(foo, list_demo))

i = 0
result = 1
while i < len(list_demo):
    result = list_demo[i] * result
    i += 1

print(result)
