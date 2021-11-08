list_demo = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

list_new = [el for el in list_demo if list_demo.count(el) == 1]

print(list_new)
