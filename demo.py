list_demo = [1, 2, 3, 4, 5, 6]

new_list = {el: el**2 for el in list_demo if el % 2 == 0}

print(new_list)
