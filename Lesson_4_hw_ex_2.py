list_demo = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


list_demo_new = [el for el in list_demo if list_demo[list_demo.index(el) - 1] < el != list_demo[0]]

print(list_demo_new)
