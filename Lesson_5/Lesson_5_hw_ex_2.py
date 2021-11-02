with open('ex_2.txt', 'r') as f:
    print(f'Количество строк = {len(f.readlines())}')
    f.seek(0)
    print({line_num + 1: len(line.split(' ')) for line_num, line in enumerate(f.readlines())})
