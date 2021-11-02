import os

dict_demo = {'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
             'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять'}

with open('ex_4.txt', 'r') as f:
    data = f.readlines()

os.remove('ex_4_new.txt')

with open('ex_4_new.txt', 'x') as f:
    i = 0
    while i < len(data):
        for key in dict_demo.keys():
            if key == data[i].split()[0]:
                f.write((dict_demo[key] + ' ' + ' '.join(data[i].split()[1:]) + '\n'))
                break
        i += 1
