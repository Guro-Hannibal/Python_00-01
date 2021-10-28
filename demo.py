list_demo = [1, 2, 3, 4, 5, 6]

expo_list = {el: el**2 for el in list_demo if el % 2 == 0}

print(expo_list)

list_demo_2 = ['wololo', 'wololo5', 'wololo', 'wololo5', 'wololo']

list_wololo = {elem + ' expo ' + '-5': int(elem)**-5 for el in list_demo_2 for elem in el if elem == '5'}

print(list_wololo)
