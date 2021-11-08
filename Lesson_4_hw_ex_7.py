def fact(a):
    factor = 1
    for el in range(1, a+1):
        factor *= el
        yield factor
    return factor


for elem in fact(4):
    print(elem)
