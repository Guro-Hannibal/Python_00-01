count = int(input('Введите колличество строк данных - '))
names_list = ['название', 'цена', 'количество', 'ед']
y = 0
master_list = []
dict_demo = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
while y < count:
    i = 0
    while i < 4:
        dict_demo[f'{names_list[i]}'] = [input(f'{names_list[i]} : ')]
        i += 1
    master_list.append((y+1, dict_demo))
    y += 1
print(count)
print(master_list)
dict_anal = {}
# i = 0
# while i < count:
#     for item in master_list[i]:
#         z = 0
#         while z < len(names_list):
#             if type(item) == type(dict_demo):
#                 print('muhaha')
#                 list_demo.append(item.get(names_list)
#             z += 1
#     i += 1

# выше осталась малая часть от трехчасового жесткого мазохизма

for data in master_list:
    for key, value in data[1].items():
        if key in dict_anal:
            dict_anal[key].append(value)
        else:
            dict_anal[key] = [value]
print(dict_anal)
