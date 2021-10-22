string = input('Введите несколько наборов символом разделенных пробелами - ')
list_string = string.split()
print(list_string)
for i in list_string:
    if len(i) > 10:
        print(f'{list_string.index(i) + 1} {i[:11]}')
    else:
        print(f'{list_string.index(i)+1} {i}')
