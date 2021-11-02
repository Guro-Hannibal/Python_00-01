with open('ex_3.txt', 'r') as f:
    dict_demo = {line.split()[0]: line.split()[1] for line in f.readlines()}
    print({item[0]: item[1] for item in dict_demo.items()})
    for key in dict_demo:
        if int(dict_demo[key]) < 200000:
            print(key, '-->', dict_demo[key])
    val_sum = 0
    for value in dict_demo.values():
        val_sum += int(value)
    print(f'Средний доход --> {val_sum / len(dict_demo)}')
